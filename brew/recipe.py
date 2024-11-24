import collections
import datetime
import json
import math
import optparse
import os.path
import sys

from .common import lfill, rfill
from . import templates

dryhop = 'dryhop'
firstwort = 'firstwort'


class Recipe:

    name = '<Recipe>'
    fermentables = []
    hops = []
    other = []
    yeast = None
    style = None
    profile = None
    batch_size = 0
    boil_time = 0
    bg = None
    og = None
    dilute_batch = 0.0
    water_in_malt = 0.0
    sparge_volume = 0.0
    mash_volume = 0.0
    mash_grav = 0.0
    late_grav = 0.0
    style_override = None
    description = None
    logs = []
    author = 'Henrik Rindlöw'

    def calc_volumes(self, malt_amount):

        if self.batch_size < self.profile.min_batch_size:
            raise TooSmallBatchError(
                f'({self.batch_size:.1f}'
                f' < {self.profile.min_batch_size:.1f})')
        boil_volume = (self.batch_size + self.profile.kettle_deadspace
                       + self.boil_time * self.profile.boil_off_rate / 60)
        if boil_volume > self.profile.max_boil_volume:
            self.dilute_batch = boil_volume - self.profile.max_boil_volume
            boil_volume = self.profile.max_boil_volume
        self.sparge_volume = 3.0
        self.water_in_malt = malt_amount * self.profile.water_in_malt_ratio
        self.mash_volume = (boil_volume + self.water_in_malt
                            - self.sparge_volume)

        if self.mash_volume > self.profile.max_mash_volume:
            self.sparge_volume += (self.mash_volume
                                   - self.profile.max_mash_volume)
            self.mash_volume = self.profile.max_mash_volume

    def calc_gravities(self, report=False):
        late_extract, potential_extract = self.calc_extract(report)

        if report:
            print('Volumes')
        wort = Wort(potential_extract * self.profile.mash_efficiency,
                    self.mash_volume, self.profile, report=report)
        wort.println('Mash')
        wort.add_water(self.sparge_volume, text='Sparge')

        wort.println('Wort', gravname='mash gravity')
        wort.remove_wort(self.water_in_malt, text='Left in malt')
        # mash_extract_ratio = wort.extract / (wort.extract + late_extract)
        late_extract_ratio = late_extract / (wort.extract + late_extract)
        self.mash_grav = wort.gravity()
        if late_extract > 0.0:
            wort.add_extract(late_extract, text='Add extract')
        wort.println('Boil Volume', gravname='boil gravity')
        self.boil_volume = wort.volume
        self.bg = wort.gravity()

        wort.boil(self.boil_time / 60, text='Boil Off')
        wort.println('After Boil', gravname='post boil gravity')

        wort.remove_wort(self.profile.kettle_deadspace, text='Left in kettle')
        if self.dilute_batch > 0.0:
            wort.add_water(self.dilute_batch, text='Dilute Batch')
        wort.println('Transferred', gravname='original gravity')
        self.transferred = wort.volume

#         self.mash_grav = (1 + wort.extract
#                           * mash_extract_ratio
#                           / wort.volume
#                           / 1000
#                           )
        self.late_grav = (1 + wort.extract
                          * late_extract_ratio
                          / wort.volume
                          / 1000)

        self.og = wort.gravity()

    def calc_extract(self, report):
        def print_separator():
            print('  ', '-' * 54)

        def print_extract(label, value):
            print(rfill('   ' + label, 42), lfill(f'{value}', 6))

        potential_extract = 0.0
        late_extract = 0.0
        if report:
            print('Extract')
        malt_amount = sum([f.amount for f in self.fermentables if f.in_mash])
        if malt_amount > self.profile.max_malt_weight:
            raise TooMuchMaltError(
                f'({malt_amount} kg '
                f'> {self.profile.max_malt_weight} kg)')
        self.calc_volumes(malt_amount)
        if report:
            print('  In Mash')
        for f in [f for f in self.fermentables if f.in_mash]:
            potential_extract += f.potential_extract(total_amount=malt_amount,
                                                     report=report)

        if report:
            print_separator()

            print_extract('Potential Extract', potential_extract)
            effective_extract = (potential_extract
                                 * self.profile.mash_efficiency)
            print_extract('Effective Extract'
                          + f' ({int(self.profile.mash_efficiency * 100)}) %',
                          effective_extract)
            print(rfill('   Malt Weight', 34),
                  lfill(f'{malt_amount:.3f} kg', 8))
        if any([not f.in_mash for f in self.fermentables]) and report:
            print('  In Kettle')
        for f in [f for f in self.fermentables if not f.in_mash]:
            late_extract += f.potential_extract(report=report)

        if report and late_extract:
            print('  ', '-' * 54)
            print_extract('Total Potential Extract',
                          potential_extract + late_extract)
            effective_extract = (potential_extract
                                 * self.profile.mash_efficiency
                                 + late_extract)
            print_extract('Total Effective Extract',
                          effective_extract)
        return late_extract, potential_extract

    def potential_extract(self):
        return sum([f.potential_extract() for f in self.fermentables])

    def estimated_extract(self):
        return self.profile.mash_efficiency * self.potential_extract()

    def gravity_report(self, report=True):
        self.calc_gravities(report=report)

    def original_gravity(self):
        if self.og is None:
            self.calc_gravities(report=False)
        return self.og

    def boil_gravity(self):
        if self.bg is None:
            self.calc_gravities(report=False)
        return self.bg

    def utilsation(self, t):
        # Tinseth
        self.boil_gravity()
        fg = 1.65 * pow(0.000125, self.bg - 1)
        ft = (1 - math.exp(-0.04 * t)) / 4.15
        return fg * ft

    def bitterness(self, report=False):
        ibu = 0
        if report:
            print('Bitterness')
        for hop in self.hops:
            if hop.minutes == dryhop:
                minutes = 0
                minstring = 'Dry-Hop'
            elif hop.minutes == firstwort:
                minutes = self.boil_time
                minstring = 'First Wort'
            else:
                minutes = hop.minutes
                minstring = f'{hop.minutes} min'
            if minutes > self.boil_time:
                print(f'Warning! Hop time {minutes} longer than boil time'
                      f' {self.boil_time}')
            b = (hop.amount * hop.alpha * self.utilsation(minutes) * 10
                 / self.batch_size)
            if hop.minutes == firstwort:
                b *= 1.1

            if report:
                print(rfill(f'   {hop.name} ({hop.alpha} %)', 20),
                      lfill(f'{hop.amount} g', 6),
                      lfill(f'({hop.alpha * hop.amount / 28.3495231:.1f} AAU)',
                            10),
                      lfill(minstring, 10),
                      lfill(f'{b:.1f}', 5))
            ibu += b
        if report:
            bugu = ibu / 1000 / (self.original_gravity() - 1)
            # rbr = bugu * (1 + self.yeast.attenuation - 0.7655)
            print('   ----------------------------------------------------')
            print(rfill('   IBU', 20), lfill(f'{ibu:.1f}', 34))
            print(rfill('   BU:GU', 20), lfill(f'{bugu:.3f}', 34))
            # print(rfill('   RBR', 20), lfill(f'{rbr:.3f}', 34))
        return ibu

    def color(self, report=False):
        mcu = 0
        if report:
            print('Color')
        for f in self.fermentables:
            mcu += f.mcu(self.batch_size, report=report)
        srm = 1.4922 * pow(mcu, 0.6859)
        ebc = srm * 1.97
        if report:
            print('   --------------------------------------------')
            print(rfill('   MCU', 20),
                  lfill(f'{mcu:.1f}', 25))
            print(rfill('   SRM', 20),
                  lfill(f'{srm:.1f}', 25))
            print(rfill('   EBC', 20),
                  lfill(f'{ebc:.1f}', 25))
        return ebc

    def final_gravity(self):
        return self.yeast.estimated_fg(self.mash_grav,
                                       self.late_grav)

    def abv(self, og=None, fg=None):
        if og is None:
            og = self.original_gravity()
        if fg is None:
            fg = self.final_gravity()
        return (og - fg) * 131

    def compliance_check(self, report=True):
        return self.style.compliance_check(self.original_gravity(),
                                           self.final_gravity(),
                                           self.abv(),
                                           self.bitterness(),
                                           self.color(),
                                           report=report)

    def html(self):
        page = templates.page()
        d = collections.defaultdict(str)
        other = ''
        d['name'] = self.name
        d['author'] = self.author
        if self.description is None:
            d['description'] = ''
        elif type(self.description) == list:
            d['description'] = '<br>'.join(self.description)
        else:
            d['description'] = self.description
        malt_amount = sum([f.amount for f in self.fermentables if f.in_mash])
        for f in self.fermentables:
            if f.in_mash:
                d['malt'] += templates.row3(
                    f.name,
                    f'{f.amount:.2f} kg',
                    f'{int(100.0 * f.amount / malt_amount)} %')
            else:
                other += templates.row3(f.name,
                                        f'{f.amount:.2f} kg',
                                        'in boil')
        d['hops'] = ''.join([hop.html() for hop in self.hops])
        d['yeast'] = self.yeast.html()
        other += ''.join([o.html() for o in self.other])
        if other:
            d['other'] = templates.other(other)
        else:
            d['other'] = ''
        d['mash'] = self.mash.html()
        d['stats'] += templates.row2('Batch size', f'{self.transferred:.1f} L')
        d['stats'] += templates.row2('Target OG',
                                     f'{self.original_gravity():.3f}')
        d['stats'] += templates.row2('Target FG',
                                     f'{self.final_gravity():.3f}')
        d['stats'] += templates.row2('Target ABV', f'{self.abv():.1f} %')
        d['stats'] += templates.row2('Target EBC', f'{self.color():.0f}')
        d['stats'] += templates.row2('Target IBU', f'{self.bitterness():.0f}')
        if self.style_override is None:
            style = self.style.code
        else:
            style = self.style_override
        d['stats'] += templates.row2('SHBF style', style)
        return(page.format(**d))

    def design(self, report=True):
        self.gravity_report(report=report)
        self.bitterness(report=report)
        self.color(report=report)
        self.compliance_check(report=report)

    def heating_time(self, start, end, volume):
        J = (end - start) * volume * 4180
        return int(J / self.profile.power / 60)

    def time_as_list(self, m):
        h = m // 60
        m %= 60
        return [h, m, 0]

    def time_as_str(self, m):
        h = m // 60
        m %= 60
        s = ''
        if h > 1:
            s += f'{h} hours'
        elif h == 1:
            s += '1 hour'
        if h > 0 and m > 0:
            s += ' and '
        if m > 1:
            s += f'{m} minutes'
        elif m == 1:
            s += '1 minute'
        return s

    def chartdata(self):
        last_temp = 15
        t = 0
        data = [[[0, 0, 0], last_temp, None, None, None]]
        first = True
        for s in self.mash.steps:
            t += self.heating_time(last_temp,
                                   s.temperature,
                                   self.mash_volume)
            if first:
                self.heattime = t
                self.mashin = s.temperature
                data.append([self.time_as_list(t),
                             s.temperature, s.temperature, None, None])
                first = False
            else:
                data.append([self.time_as_list(t),
                             None, s.temperature, None, None])
                t += s.time
                data.append([self.time_as_list(t),
                             None, s.temperature, None, None])
            last_temp = s.temperature

        self.mashtime = t - self.heattime
        data.append([self.time_as_list(t),
                     None, None, s.temperature, None])

        self.boilup = self.heating_time(last_temp, 100, self.boil_volume)
        t += self.boilup
        data.append([self.time_as_list(t),
                     None, None, 100, None])
        t += self.boil_time
        data.append([self.time_as_list(t),
                     None, None, 100, 100])
        t += 30
        data.append([self.time_as_list(t),
                     None, None, None, 20])

        return json.dumps(data)

    def program(self):
        p = ''
        i = 0
        for s in self.mash.steps:
            if s.name == 'Mash In':
                p += templates.row3('Mashing', f'{s.temperature} °C', '&nbsp;')
            else:
                p += templates.row3(f'Step {i}',
                                    f'{s.temperature} °C',
                                    f'{s.time:03d} min')
            i += 1
        while i < 6:
            p += templates.row3(f'Step {i}',
                                f'{s.temperature} °C',
                                '000 min')
            i += 1
        p += templates.row3('Boiling', '100 °C', f'{self.boil_time:03d} min')
        times = set([f'{h.minutes: 3d}' for h in self.hops
                     if type(h.minutes) == int])
        hops = '/'.join(sorted(times, reverse=True))
        p += templates.row2b('Hop additions', f'{hops} min')
        return p

    def instructions(self):
        page = templates.instructions()
        d = collections.defaultdict(str)
        d['name'] = self.name
        d['author'] = self.author
        if self.description is None:
            d['description'] = ''
        elif type(self.description) == list:
            d['description'] = '<br>'.join(self.description)
        else:
            d['description'] = self.description
        d['other'] = ''
        for f in self.fermentables:
            if f.in_mash:
                d['malt'] += templates.row2(
                    f.name,
                    f'{f.amount:.2f} kg')
            else:
                d['other'] += templates.row3(f'{self.boil_time} min', f.name,
                                             f'{f.amount:.2f} kg')
        d['other'] += ''.join([hop.instructions() for hop in self.hops
                               if hop.minutes != dryhop])
        d['fermenter'] = self.yeast.html()
        d['fermenter'] += ''.join([hop.fermenter() for hop in self.hops
                                   if hop.minutes == dryhop])
        d['other'] += ''.join([o.html() for o in self.other])
        d['chartdata'] = self.chartdata()
        d['program'] = self.program()
        d['mashvol'] = self.mash_volume
        d['heattime'] = self.time_as_str(self.heattime)
        d['mashtime'] = self.time_as_str(self.mashtime)
        d['mashin'] = self.mashin
        d['spargevol'] = self.sparge_volume
        d['boilup'] = self.time_as_str(self.boilup)
        d['mashgrav'] = self.mash_grav
        d['og'] = self.og

        return(page.format(**d))

    def run(self):
        parser = optparse.OptionParser()
        parser.add_option('-r', '--recipe', action='store_true', dest='recipe')
        parser.add_option('-i', '--instructions', action='store_true',
                          dest='instructions')
        options, args = parser.parse_args(sys.argv)
        if options.recipe:
            self.design(report=False)
            base, ext = os.path.splitext(os.path.basename(args[0]))
            with open(base + '_recipe.html', 'w') as f:
                f.write(self.html())
        elif options.instructions:
            self.design(report=False)
            base, ext = os.path.splitext(os.path.basename(args[0]))
            with open(base + '_instructions.html', 'w') as f:
                f.write(self.instructions())
        else:
            self.design(report=True)
            self.printlog()

    def log(self,
            brew_date=None,
            mash_gravity=None,
            original_gravity=None,
            racking_date=None,
            final_gravity=None):
        self.logs.append((brew_date,
                          mash_gravity,
                          original_gravity,
                          racking_date,
                          final_gravity))

    def printlog(self):
        for (brew_date, mash_gravity, original_gravity, racking_date,
             final_gravity) in self.logs:
            print()
            if brew_date is not None:
                print(f'Brew day {brew_date}')
            if mash_gravity is not None:
                print(f'  Mash gravity {mash_gravity:.3f}'
                      f', estimated {self.mash_grav:.3f}')
            if original_gravity is not None:
                print(f'  OG {original_gravity:.3f}, estimated {self.og:.3f}')
            if racking_date is not None:
                print(f' Racked {racking_date}')
            if brew_date is not None and racking_date is not None:
                ferm = (datetime.date.fromisoformat(racking_date)
                        - datetime.date.fromisoformat(brew_date))
                print(f'  Fermentation time {ferm.days} days')
            if final_gravity is not None:
                print(f'  FG {final_gravity:.3f}'
                      f', estimated {self.final_gravity():.3f}')
            if original_gravity is not None and final_gravity is not None:
                print(f'  ABV {self.abv(original_gravity, final_gravity):.1f}'
                      f' %, estimated {self.abv():.1f} %')


class Ingredient:

    def __init__(self, name, amount, when):
        self.name = name
        self.amount = amount
        self.when = when

    def html(self):
        return templates.row3(self.name, self.amount, self.when)


class MashSchedule:

    def __init__(self, steps):
        self.steps = steps
        self.double = False

    def program(self):
        print('Mash Schedule')
        for step in self.steps:
            print(' ', rfill(step.name, 20),
                  lfill(str(step.temperature), 5),
                  lfill(str(step.time), 5))

    def html(self):
        return ''.join([step.html() for step in self.steps])


class SingleStepMashWithMashOut(MashSchedule):

    def __init__(self, temp):
        MashSchedule.__init__(self, [Step(60, 0, 'Mash In'),
                                     Step(temp, 60, 'Saccharification rest'),
                                     Step(77, 10, 'Mash Out')])


class SingleStepMash(MashSchedule):

    def __init__(self, temp):
        MashSchedule.__init__(self, [Step(60, 0, 'Mash In'),
                                     Step(temp, 60, 'Saccharification rest')])


class DoubleSingleStepMashWithMashOut(SingleStepMashWithMashOut):

    def __init__(self, temp):
        super.__init__(temp)
        self.double = True


class Step:

    def __init__(self, temperature, minutes, name):
        self.temperature = temperature
        self.time = minutes
        self.name = name

    def html(self):
        if self.time == 0:
            return templates.row3(self.name, '&nbsp;',
                                  f'{self.temperature} °C')
        else:
            return templates.row3(self.name,
                                  f'{self.time} min',
                                  f'{self.temperature} °C')


class TooMuchMaltError(Exception):
    pass


class TooSmallBatchError(Exception):
    pass


class Wort:

    def __init__(self, extract, water, profile, report=False):
        self.extract = extract
        self.volume = water
        self.report = report
        self.profile = profile

    def gravity(self):
        return 1 + self.extract / self.volume / 1000.0

    def add_water(self, volume, text=None):
        if self.report:
            print('  ', rfill(text, 20),
                  ' ', lfill(f'{volume:.1f}', 4),
                  ' ', lfill('0.0', 6),
                  ' ', lfill('1.000', 5))
        self.volume += volume

    def add_extract(self, extract, text=None):
        if self.report:
            print('  ', rfill(text, 20),
                  ' ', lfill('0.0', 4),
                  ' ', lfill(f'{extract:.1f}', 6),
                  ' ', lfill('', 5))
        self.extract += extract

    def boil(self, hours, text=None):
        rate = self.profile.boil_off_rate
        self.volume -= (rate * hours)
        if self.report:
            print('  ', rfill(text, 20),
                  ' ', lfill(f'{-rate * hours:.1f}', 4),
                  ' ', lfill('0.0', 6),
                  ' ', lfill('1.000', 5))

    def remove_wort(self, volume, text=None):
        if self.report:
            print('  ', rfill(text, 20),
                  ' ', lfill(f'{-volume:.1f}', 4),
                  ' ', lfill(f'{-volume * self.extract / self.volume:.1f}', 6),
                  ' ', lfill(f'{self.gravity():.3f}', 5))
        self.extract -= (volume * self.extract / self.volume)
        self.volume -= volume

    def println(self, text, gravname=''):
        if self.report:
            print('   --------------------------------------------')
            print('  ', rfill(text, 20),
                  ' ', lfill(f'{self.volume:.1f}', 4),
                  ' ', lfill(f'{self.extract:.1f}', 6),
                  ' ', lfill(f'{self.gravity():.3f}', 5),
                  ' ', gravname)

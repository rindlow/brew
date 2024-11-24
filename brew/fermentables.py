# -*- coding: utf-8 -*-

from .common import lfill, rfill


class Fermentable:

    in_mash = True
    potential = 0.0
    color = 0.0
    name = '<fermentable>'

    def __init__(self, amount):
        self.amount = amount

    def potential_extract_per_kg(self):
        return 46 * 8.3454 * self.potential

    def potential_extract(self, total_amount=None, report=False):
        if report:
            if total_amount is None:
                percent = ''
            else:
                percent = lfill(f'{100.0 * self.amount / total_amount:.1f} %',
                                7)
            print('  ', rfill(self.name, 20),
                  ' ', lfill(f'{self.potential_extract_per_kg():.1f}', 5),
                  ' ', lfill(f'{self.amount:.3f}', 6),
                  ' ', lfill(f'{self.potential_extract():.1f}', 6),
                  percent)
        return self.potential_extract_per_kg() * self.amount

    def mcu(self, batch_size, report=False):
        if self.color == 0:
            mcu = 0.0
        else:
            srm = self.color * 0.508
            lovibond = (srm + 0.76) / 1.3546
            mcu = self.amount * (lovibond * 2.205) / (batch_size * 0.264)
        if report:
            print(rfill(f'   {self.name}', 23),
                  lfill(f'{self.color} EBC', 10),
                  lfill(f'{self.amount:.2f} kg', 8),
                  lfill(f'{mcu:.1f}', 5))
        return mcu


class WhiteSugar(Fermentable):
    name = 'White Sugar'
    potential = .99
    color = 0
    in_mash = False


class Amylase(Fermentable):
    name = 'Amylase'
    potential = 0
    color = 0
    in_mash = False
    is_amylase = True


class CandiSyrup(Fermentable):
    name = 'Candi Syrup'
    potential = .70
    color = 354
    in_mash = False


class FlakedBarley(Fermentable):
    name = 'Flaked Barley'
    potential = .7
    color = 4


class FlakedMaize(Fermentable):
    name = 'Flaked Maize'
    potential = .865
    color = 0.75


class GoldenSyrup(Fermentable):
    name = 'Golden Syrup'
    potential = .79
    color = 100
    in_mash = False


class DextrinMalt(Fermentable):
    name = 'Dextrin Malt'
    potential = .70
    color = 3.0


class Pilsen6RW(Fermentable):
    name = 'Pilsen 6RW'
    potential = .80
    color = 3.4


class PilsnerMalt(Fermentable):
    name = 'Pilsner Malt'
    potential = .80
    color = 3.5


class WheatMalt(Fermentable):
    name = 'Wheat Malt'
    potential = .82
    color = 4


class CaraPils(Fermentable):
    name = 'CaraPils'
    potential = .75
    color = 4.5


class PaleAleMalt(Fermentable):
    name = 'Pale Ale Malt'
    potential = .79
    color = 6.5


class MarisOtterAleMalt(Fermentable):
    name = 'Maris Otter Ale Malt'
    potential = .815
    color = 6.5


class ViennaMalt(Fermentable):
    name = 'Vienna Malt'
    potential = .8
    color = 7.0


class AshburneMildMalt(Fermentable):
    name = 'Ashburne Mild Malt'
    potential = .76
    color = 10


class CaraGold(Fermentable):
    name = 'Cara Gold Malt'
    potential = .68
    color = 15


class MunichI(Fermentable):
    name = 'Münich Malt Type 1'
    potential = .78
    color = 15


class DarkMunich(Fermentable):
    name = 'Dark Münich Malt'
    potential = .78
    color = 50


class CaraRuby(Fermentable):
    name = 'CaraRuby'
    potential = .78
    color = 50


class Aromatic(Fermentable):
    name = 'Aromatic Malt'
    potential = .79
    color = 50


class BiscuitMalt(Fermentable):
    name = 'Biscuit Malt'
    potential = .75
    color = 60


class AmberMalt(Fermentable):
    name = 'Amber Malt'
    potential = .70
    color = 65


class MelanoidinMalt(Fermentable):
    name = 'Melanoidin Malt'
    potential = .75
    color = 70


class CaraMunichI(Fermentable):
    name = 'Caramünich Type 1'
    potential = .73
    color = 80


class CaraMunichII(Fermentable):
    name = 'Caramünich Type 2'
    potential = .73
    color = 120


class BrownMalt(Fermentable):
    name = 'Brown Malt'
    potential = .70
    color = 135


class Crystal100(Fermentable):
    name = 'Crystal 100'
    potential = .74
    color = 100


class Crystal150(Fermentable):
    name = 'Crystal 150'
    potential = .74
    color = 150


class Crystal240(Fermentable):
    name = 'Crystal 240'
    potential = .72
    color = 240


class SpecialB(Fermentable):
    name = 'Special B'
    potential = .72
    color = 300


class CaraAroma(Fermentable):
    name = 'CaraAroma'
    potential = .74
    color = 350


class ChocolateMalt(Fermentable):
    name = 'Chocolate Malt'
    potential = .65
    color = 1000


class BlackMalt(Fermentable):
    name = 'Black Malt'
    potential = .715
    color = 1300


class Caramel(Fermentable):
    name = 'Caramel (E150)'
    potential = 0
    color = 10000
    in_mash = False

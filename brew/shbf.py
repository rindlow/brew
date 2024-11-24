from .common import slider


class Style:

    min_og = 0.0
    max_og = 0.0
    min_fg = 0.0
    max_fg = 0.0
    min_abv = 0.0
    max_abv = 0.0
    min_ibu = 0.0
    max_ibu = 0.0
    min_ebc = 0.0
    max_ebc = 0.0

    def compliance_check(self, og, fg, abv, ibu, ebc, report=True):

        compliant = True
        if report:
            print('Style')

        if self.min_og <= round(og, 3) <= self.max_og:
            if report:
                slider('OG', self.min_og, self.max_og, og, '%.3f')
        else:
            compliant = False
            if report:
                print(f'   OG {og:.3f} not in range',
                      f'{self.min_og} - {self.max_og}')

        if self.min_fg <= round(fg, 3) <= self.max_fg:
            if report:
                slider('FG', self.min_fg, self.max_fg, fg, '%.3f')
        else:
            compliant = False
            if report:
                print(f'   FG {fg:.3f} not in range',
                      f'{self.min_fg:.3f} - {self.max_fg:.3f}')

        if self.min_abv <= round(abv, 1) <= self.max_abv:
            if report:
                slider('ABV', self.min_abv, self.max_abv, abv, '%.1f')
        else:
            compliant = False
            if report:
                print(f'   ABV {abv:.1f} not in range',
                      f'{self.min_abv} - {self.max_abv}')

        if self.min_ibu <= round(ibu, 0) <= self.max_ibu:
            if report:
                slider('IBU', self.min_ibu, self.max_ibu, ibu, '%.0f')
        else:
            compliant = False
            if report:
                print(f'   IBU {ibu:.0f} not in range',
                      f'{self.min_ibu} - {self.max_ibu}')

        if self.min_ebc <= round(ebc, 0) <= self.max_ebc:
            if report:
                slider('EBC', self.min_ebc, self.max_ebc, ebc, '%.0f')
        else:
            compliant = False
            if report:
                print(f'   EBC {ebc:.0f} not in range',
                      f'{self.min_ebc} - {self.max_ebc}')

        return compliant


class Helles(Style):
    code = '1A'
    min_og = 1.044
    max_og = 1.050
    min_fg = 1.008
    max_fg = 1.012
    min_abv = 4.5
    max_abv = 5.2
    min_ibu = 15
    max_ibu = 24
    min_ebc = 7
    max_ebc = 14


class Marzen(Style):
    code = '1C'
    min_og = 1.048
    max_og = 1.060
    min_fg = 1.010
    max_fg = 1.018
    min_abv = 4.8
    max_abv = 5.9
    min_ibu = 18
    max_ibu = 24
    min_ebc = 15
    max_ebc = 34

class FranconianLager(Style):
    code = '1D'
    min_og = 1.044
    max_og = 1.055
    min_fg = 1.008
    max_fg = 1.015
    min_abv = 4.5
    max_abv = 5.5
    min_ibu = 25
    max_ibu = 35
    min_ebc = 15
    max_ebc = 59

class CzechPilsener(Style):
    code = '1G'
    min_og = 1.044
    max_og = 1.050
    min_fg = 1.010
    max_fg = 1.014
    min_abv = 4.0
    max_abv = 5.0
    min_ibu = 25
    max_ibu = 40
    min_ebc = 11
    max_ebc = 14


class Bock(Style):
    code = '2A'
    min_og = 1.066
    max_og = 1.074
    min_fg = 1.012
    max_fg = 1.020
    min_abv = 6.3
    max_abv = 7.5
    min_ibu = 17
    max_ibu = 27
    min_ebc = 11
    max_ebc = 60


class EnglishDarkMild(Style):
    code = '3A'
    min_og = 1.032
    max_og = 1.037
    min_fg = 1.006
    max_fg = 1.011
    min_abv = 3.0
    max_abv = 3.7
    min_ibu = 10
    max_ibu = 24
    min_ebc = 40
    max_ebc = 90


class EnglishOrdinaryBitter(Style):
    code = '3F'
    min_og = 1.034
    max_og = 1.040
    min_fg = 1.006
    max_fg = 1.012
    min_abv = 3.4
    max_abv = 4.0
    min_ibu = 20
    max_ibu = 40
    min_ebc = 16
    max_ebc = 30


class EnglishBestBitter(Style):
    code = '4A'
    min_og = 1.040
    max_og = 1.046
    min_fg = 1.006
    max_fg = 1.012
    min_abv = 3.7
    max_abv = 4.8
    min_ibu = 20
    max_ibu = 40
    min_ebc = 25
    max_ebc = 35


class AmericanPaleAle(Style):
    code = '4C'
    min_og = 1.044
    max_og = 1.056
    min_fg = 1.008
    max_fg = 1.016
    min_abv = 4.4
    max_abv = 5.9
    min_ibu = 20
    max_ibu = 35
    min_ebc = 12
    max_ebc = 28


class EnglishIPA(Style):
    code = '4E'
    min_og = 1.050
    max_og = 1.065
    min_fg = 1.010
    max_fg = 1.016
    min_abv = 5.0
    max_abv = 6.5
    min_ibu = 40
    max_ibu = 60
    min_ebc = 25
    max_ebc = 40


class StrongPaleAle(Style):
    code = '5B'
    min_og = 1.057
    max_og = 1.072
    min_fg = 1.012
    max_fg = 1.018
    min_abv = 5.9
    max_abv = 7.5
    min_ibu = 30
    max_ibu = 50
    min_ebc = 20
    max_ebc = 35


class AmericanIPA(Style):
    code = '5C'
    min_og = 1.056
    max_og = 1.070
    min_fg = 1.010
    max_fg = 1.016
    min_abv = 5.9
    max_abv = 7.5
    min_ibu = 50
    max_ibu = 75
    min_ebc = 15
    max_ebc = 25


class BarleyWine(Style):
    code = '5G'
    min_og = 1.083
    max_og = 1.200              # Unlimited
    min_fg = 1.018
    max_fg = 1.030              # Unlimited
    min_abv = 8.5
    max_abv = 12                # Unlimited
    min_ibu = 50
    max_ibu = 100
    min_ebc = 30
    max_ebc = 75


class Porter(Style):
    code = '7D'
    min_og = 1.053
    max_og = 1.063
    min_fg = 1.015
    max_fg = 1.022
    min_abv = 5.0
    max_abv = 6.2
    min_ibu = 20
    max_ibu = 40
    min_ebc = 60
    max_ebc = 100


class ImperialPorter(Style):
    code = '8C'
    min_og = 1.064
    max_og = 1.090
    min_fg = 1.015
    max_fg = 1.030
    min_abv = 6.3
    max_abv = 9.5
    min_ibu = 35
    max_ibu = 65
    min_ebc = 60
    max_ebc = 100


class Tripel(Style):
    code = '9C'
    min_og = 1.070
    max_og = 1.090
    min_fg = 1.008
    max_fg = 1.013
    min_abv = 7.5
    max_abv = 10.5
    min_ibu = 20
    max_ibu = 39
    min_ebc = 7
    max_ebc = 20


class DarkStrongBelgianAle(Style):
    code = '9G'
    min_og = 1.068
    max_og = 1.200              # Unlimited
    min_fg = 1.010
    max_fg = 1.018
    min_abv = 7.5
    max_abv = 13.0
    min_ibu = 20
    max_ibu = 35
    min_ebc = 30
    max_ebc = 75


class Saison(Style):
    code = '9H'
    min_og = 1.044
    max_og = 1.056
    min_fg = 1.002
    max_fg = 1.008
    min_abv = 5.0
    max_abv = 6.8
    min_ibu = 20
    max_ibu = 35
    min_ebc = 5
    max_ebc = 35

# -*- coding: utf-8 -*-

from . import templates


class Yeast:

    attenuation = .75
    sugar_attenuation = 1.225   # Estimated, no calculation behind

    def estimated_fg(self, mash, sugar):
        mash_points = 1000 * (mash - 1)
        sugar_points = 1000 * (sugar - 1)
        points = (mash_points * (1 - self.attenuation)
                  + sugar_points * (1 - self.sugar_attenuation))
        return 1 + (points / 1000)

    def html(self):
        return templates.row1(self.name)


class BavarianLager(Yeast):
    name = "Bavarian Lager - Mangrove Jack's M76"
    attenuation = 0.75


class BelgianAle(Yeast):
    name = "Belgian Ale - Mangrove Jack's M41"
    attenuation = 0.75


class BelgianSaison(Yeast):
    name = 'Belgian Saison - Wyeast 3724'
    attenuation = 0.77


class BelgianStrongAle(Yeast):
    name = 'Belgian Strong Ale - Wyeast 1388'
    attenuation = 0.75


class BohemianLager(Yeast):
    name = "Bohemian Lager - Mangrove Jack's M84"
    attenuation = 0.74


class CzechBudejoviceLager(Yeast):
    name = 'Czech Budejovice Lager - WLP802'
    attenuation = 0.77


class EmpireAle(Yeast):
    name = "Empire Ale - Mangrove Jack's M15"
    attenuation = 0.72


class GermanAleKolsch(Yeast):
    name = 'German Ale/Kölsch - WLP029'
    attenuation = 0.75


class LibertyBellAle(Yeast):
    name = "Liberty Bell Ale - Mangrove Jack's M36"
    attenuation = 0.76


class LondonAleIII(Yeast):
    name = 'London Ale III - Wyeast 1318'
    attenuation = 0.73


class LondonESBAle(Yeast):
    name = 'London ESB Ale - Wyeast 1968'
    attenuation = 0.69


class Nottingham(Yeast):
    name = 'Lallemand Nottingham Ale'
    attenuation = 0.81


class S04(Yeast):
    name = 'Safale S-04 (Whitbread)'
    attenuation = 0.73


class US05(Yeast):
    name = 'Safale US-05'
    attenuation = 0.73


class SaflagerW34_70(Yeast):
    name = 'Saflager W-34/70'
    attenuation = 0.75


class SouthernGermanLager(Yeast):
    name = 'Southern German Lager - WLP838'
    attenuation = 0.73


class TrappistHighGravity(Yeast):
    name = 'Trappist High Gravity - Wyeast 3789'
    attenuation = 0.76


class WhitbreadAle(Yeast):
    name = 'Whitbread Ale - Wyeast 1099'
    attenuation = 0.70


class WestYorkshireAle(Yeast):
    name = 'West Yorkshire Ale - Wyeast 1469'
    attenuation = 0.69

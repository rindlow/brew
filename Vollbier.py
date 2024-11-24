#!/usr/bin/env python

#  https://www.maischemalzundmehr.de/index.php?inhaltmitte=rezept&id=359&suche_begriff=fränk&suche_sorte=Dunkles+Lager&factoraw=19&factorsha=63.2&factorhav=7&factorha1=7&factorha2=7

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    PilsnerMalt,
    ViennaMalt,
    CaraRuby,
    ChocolateMalt,
)
from brew.hops import (
    HallertauTradition,
    Perle
)
import brew.shbf
from brew.yeast import SaflagerW34_70


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Fränkisches Vollbier"
        self.style = brew.shbf.FranconianLager()
        self.profile = Braumeister20l()
        self.fermentables = [
            PilsnerMalt(3.0),
            ViennaMalt(1.5),
            CaraRuby(1.25),
            ChocolateMalt(0.15),
        ]
        self.hops = [
            HallertauTradition(15, 60, alpha=6.0),
            Perle(20, 60, alpha=5.4),
            HallertauTradition(15, 15, alpha=6.0)]
        self.yeast = SaflagerW34_70()
        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 19


if __name__ == "__main__":
    recipe = Recipe()
    recipe.log(
        brew_date="2023-07-08",
        original_gravity=1.054,
        racking_date="2023-08-05",
        final_gravity=1.013,
    )
    recipe.run()

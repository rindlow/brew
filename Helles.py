#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    Pilsen6RW,
    CaraGold
)
from brew.hops import (
    HallertauerMittelfruh,
    NorthernBrewer
)
from brew.shbf import Helles
from brew.yeast import BavarianLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Helles"
        self.style = Helles()
        self.profile = Braumeister20l()
        self.fermentables = [
            Pilsen6RW(5.0),
            CaraGold(0.3)
        ]
        self.hops = [
            NorthernBrewer(20, 60),
            HallertauerMittelfruh(10, 10)
        ]
        self.yeast = BavarianLager()
        self.mash = brew.SingleStepMashWithMashOut(69)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

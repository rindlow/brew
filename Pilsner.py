#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    PilsnerMalt,
    MelanoidinMalt,
    CaraPils
)
from brew.hops import (
    Saaz,
    NorthernBrewer
)
from brew.shbf import CzechPilsener
from brew.yeast import CzechBudejoviceLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Pilsner"
        self.style = CzechPilsener()
        self.profile = Braumeister20l()
        self.fermentables = [
            PilsnerMalt(5.0),
            MelanoidinMalt(0.3),
            CaraPils(0.3),
        ]
        self.hops = [
            Saaz(40, 60, alpha=2.2),
            NorthernBrewer(8, 60, alpha=10.4),
            Saaz(20, 40, alpha=2.2),
            Saaz(30, 20, alpha=2.2),
        ]
        self.yeast = CzechBudejoviceLager()
        self.mash = brew.SingleStepMashWithMashOut(68)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2020-01-26",
        original_gravity=1.053,
        racking_date="2020-03-07",
        final_gravity=1.015,
    )

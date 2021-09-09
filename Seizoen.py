#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    PilsnerMalt,
    CaraPils,
    WhiteSugar
)
from brew.hops import Bobek
from brew.shbf import Saison
from brew.yeast import BelgianSaison


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Seizoen"
        self.style = Saison()
        self.profile = Braumeister20l()
        self.fermentables = [
            PilsnerMalt(4.7),
            CaraPils(0.3),
            WhiteSugar(0.75)
        ]
        self.hops = [
            Bobek(40, 90),
            Bobek(20, 5)
        ]
        self.yeast = BelgianSaison()
        self.mash = brew.SingleStepMashWithMashOut(63)
        self.boil_time = 90
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

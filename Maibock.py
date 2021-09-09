#!/usr/bin/env python

import brew
from brew.fermentables import (
    MarisOtterAleMalt,
    PilsnerMalt,
    DarkMunich,
)
from brew.hops import (
    HallertauerMittelfruh,
    Magnum
)
from brew.profiles import Braumeister20l
from brew.shbf import Bock
from brew.yeast import BavarianLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Armadillo"
        self.description = "Strong Pale Ale"
        self.style = Bock()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(2.4),
            DarkMunich(1.2),
            PilsnerMalt(2.4),
        ]
        self.hops = [
            HallertauerMittelfruh(20, brew.firstwort),
            Magnum(5, 60)
        ]
        self.yeast = BavarianLager()
        self.mash = brew.SingleStepMashWithMashOut(65)
        self.boil_time = 60
        self.batch_size = 14


recipe = Recipe()
recipe.run()

#!/usr/bin/env python

import brew
from brew.fermentables import (
    MarisOtterAleMalt,
    Crystal100,
    MunichI,
)
from brew.hops import Amarillo
from brew.profiles import Braumeister20l
from brew.shbf import StrongPaleAle
from brew.yeast import US05


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Armadillo"
        self.description = "Strong Pale Ale"
        self.style = StrongPaleAle()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(5.1),
            MunichI(0.6),
            Crystal100(0.3),
        ]
        self.hops = [
            Amarillo(30, brew.firstwort, alpha=7.3),
            Amarillo(30, brew.dryhop, alpha=7.3),
        ]
        self.yeast = US05()
        self.mash = brew.SingleStepMashWithMashOut(65)
        self.boil_time = 60
        self.batch_size = 16


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2020-07-17",
        original_gravity=1.061,
        final_gravity=1.014
    )

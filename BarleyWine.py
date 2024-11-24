#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    SpecialB,
    Crystal100,
    GoldenSyrup,
    WhiteSugar,
)
from brew.hops import Target, BramblingCross
from brew.shbf import BarleyWine
from brew.yeast import EmpireAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Barley Wine"
        self.style = BarleyWine()
        self.description = "English Barley Wine"
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(5.6),
            SpecialB(0.2),
            Crystal100(0.2),
            GoldenSyrup(1.5),
            WhiteSugar(0.25),
        ]
        self.hops = [
            Target(40, 60),
            BramblingCross(30, 20),
        ]
        self.yeast = EmpireAle()
        self.mash = brew.SingleStepMashWithMashOut(69)
        self.boil_time = 60
        self.batch_size = 16


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
#     recipe.log(
#         brew_date="2018-09-29",
#         original_gravity=1.076,
#         racking_date="2018-10-13",
#         final_gravity=1.01,
#     )

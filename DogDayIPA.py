#!/usr/bin/env python

import brew
from brew.fermentables import (
    MarisOtterAleMalt,
    CaraGold,
    Pilsen6RW,
    WhiteSugar,
)
from brew.hops import Amarillo, Simcoe


class Recipe(brew.Recipe):
    def __init__(self):

        self.name = "Dog Day IPA"
        self.style = brew.shbf.AmericanIPA()
        self.description = "American IPA"
        self.profile = brew.profiles.Braumeister20l()

        self.fermentables = [
            MarisOtterAleMalt(3.0),
            CaraGold(1.5),
            Pilsen6RW(1.0),
            WhiteSugar(0.4),
        ]

        self.hops = [
            Simcoe(24, 60, alpha=12.5),
            Simcoe(20, 10, alpha=12.5),
            Amarillo(20, 10, alpha=7.5),
            Simcoe(30, 0, alpha=12.5),
            Amarillo(30, 0, alpha=7.5),
            Simcoe(26, brew.dryhop,  alpha=12.5),
            Amarillo(50, brew.dryhop, alpha=7.5),
        ] # 60 IBU

        self.yeast = brew.yeast.US05()

        self.mash = brew.SingleStepMash(67)

        self.boil_time = 60
        self.batch_size = 16


if __name__ == "__main__":
    recipe = Recipe()
    recipe.log(
        brew_date="2021-07-24",
        mash_gravity=1.050,
        original_gravity=1.064,
        racking_date="2021-08-14",
        final_gravity=1.014,
    )  
    recipe.log(
        brew_date="2022-11-26",
        mash_gravity=1.046,
        original_gravity=1.058,
        racking_date="2022-12-04",
        final_gravity=1.011,
    )
    recipe.run()


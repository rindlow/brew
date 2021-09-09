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
            Simcoe(20, 60),
            Simcoe(20, 10),
            Amarillo(20, 10),
            Simcoe(30, 0),
            Amarillo(30, 0),
            Simcoe(30, brew.dryhop),
            Amarillo(50, brew.dryhop),
        ]

        self.yeast = brew.yeast.US05()

        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 16


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2021-07-24",
        mash_gravity=1.050,
        original_gravity=1.064,
        racking_date="2021-08-14",
        final_gravity=1.014,
    )

#!/usr/bin/env python

from curses.ascii import US
import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    ChocolateMalt,
    PaleAleMalt,
    WhiteSugar,
)
from brew.hops import (
    Fuggle,
    BramblingCross
)
import brew.shbf
from brew.yeast import US05


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Bitter"
        self.style = brew.shbf.EnglishOrdinaryBitter()
        self.style_override = '3F'
        self.profile = Braumeister20l()
        self.fermentables = [
            PaleAleMalt(3.0),
            ChocolateMalt(0.1),
            # WhiteSugar(0.25),
        ]
        self.hops = [
            Fuggle(30, 60),
            BramblingCross(10, 20),
            BramblingCross(10, 0)
        ]
        self.yeast = US05()
        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()

    # recipe.log(
    #     brew_date="2021-09-05",
    #     original_gravity=1.053,
    #     racking_date="2021-10-13",
    #     final_gravity=1.015,
    # )
    recipe.run()

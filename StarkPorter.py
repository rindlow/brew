#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    MunichI,
    Crystal240,
    BrownMalt,
    ChocolateMalt,
    WhiteSugar,
)
from brew.hops import Magnum
from brew.shbf import ImperialPorter
from brew.yeast import LondonESBAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Starkporter"
        self.style = ImperialPorter()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(1.75),
            MunichI(3.5),
            BrownMalt(0.25),
            Crystal240(0.25),
            ChocolateMalt(0.25),
            WhiteSugar(0.6),
        ]
        self.hops = [Magnum(30, 60)]
        self.yeast = LondonESBAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 15


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2019-01-06",
        original_gravity=1.074,
        racking_date="2019-02-21",
        final_gravity=1.014,
    )

#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    Crystal150,
    BrownMalt,
    ChocolateMalt,
)
from brew.hops import Fuggle
from brew.shbf import Porter
from brew.yeast import LondonESBAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "London Bridge"
        self.description = "English Porter"
        self.style = Porter()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(4.5),
            BrownMalt(0.8),
            Crystal150(0.6),
            ChocolateMalt(0.4),
        ]
        self.hops = [
            Fuggle(35, 60, alpha=5.9),
            Fuggle(15, 10, alpha=5.9)
        ]
        self.yeast = LondonESBAle()
        self.mash = brew.SingleStepMashWithMashOut(66)
        self.boil_time = 60
        self.batch_size = 18


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2020-11-22",
        original_gravity=1.056,
        racking_date="2020-12-05",
        final_gravity=1.014,
    )

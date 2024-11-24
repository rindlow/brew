#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    CaraAroma,
    GoldenSyrup,
)
from brew.hops import (
    EastKentGoldings,
    NorthernBrewer,
)
import brew.shbf
from brew.yeast import Nottingham


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Best Bitter"
        self.style = brew.shbf.EnglishBestBitter()
        self.style_override = '4A'
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(4.0),
            CaraAroma(0.4),
            GoldenSyrup(0.4),
        ]
        self.hops = [
            EastKentGoldings(50, 30),
            NorthernBrewer(50, 5),
            EastKentGoldings(30, 1)
        ]
        self.yeast = Nottingham()
        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()

    recipe.log(
        brew_date="2024-11-24",
        original_gravity=1.049,
        racking_date="2024-12-24",
        final_gravity=1.012,
    )
    recipe.run()

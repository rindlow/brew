#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import MarisOtterAleMalt, GoldenSyrup, DextrinMalt
from brew.hops import Fuggle, BramblingCross
from brew.shbf import EnglishIPA
from brew.yeast import WhitbreadAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "1914 Whitbread X"
        self.style = EnglishIPA()
        self.description = "Mild"
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(2.25),
            DextrinMalt(0.25),
            GoldenSyrup(0.3),
        ]
        self.hops = [
            Fuggle(24, 30, alpha=4.3),
            Fuggle(18, 15, alpha=4.3),
            BramblingCross(6, 15, alpha=6.7),
            BramblingCross(10, 0, alpha=6.7),
        ]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(72)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2020-08-02",
        original_gravity=1.031,
        racking_date="2020-08-11",
        final_gravity=1.014,
    )

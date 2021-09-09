#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    GoldenSyrup,
    DextrinMalt
)
from brew.hops import (
    Fuggle,
    Enigma
)
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
            Fuggle(30, 60, alpha=4.3),
            Fuggle(30, 30, alpha=4.3),
            Enigma(5, 10, alpha=16.4),
        ]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(75)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2020-05-17",
        original_gravity=1.032,
        racking_date="2020-05-30",
        final_gravity=1.008,
    )

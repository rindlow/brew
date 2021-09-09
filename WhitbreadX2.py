#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    GoldenSyrup
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
            MarisOtterAleMalt(5.0),
            GoldenSyrup(0.75)
        ]
        self.hops = [
            Enigma(10, 60),
            Fuggle(30, 30, alpha=4.3),
            Fuggle(30, 15, alpha=4.3),
            Enigma(5, 10),
        ]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(64)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2019-08-10",
        original_gravity=1.059,
        racking_date="2019-09-06",
        final_gravity=1.013,
    )

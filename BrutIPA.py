#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    PaleAleMalt,
    FlakedMaize,
    Amylase
)
from brew.hops import Perle
from brew.shbf import AmericanIPA
from brew.yeast import LibertyBellAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Brut IPA"
        self.style = AmericanIPA()
        self.profile = Braumeister20l()
        self.fermentables = [
            PaleAleMalt(5),
            FlakedMaize(0.5)
        ]
        self.hops = [
            Perle(5, 15),
            Perle(75, 0)
        ]
        self.other = [
            Amylase(0.01)
        ]
        self.yeast = LibertyBellAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

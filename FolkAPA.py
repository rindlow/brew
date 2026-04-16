#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    MunichI,
    WheatMalt,
    GoldenSyrup,
)
from brew.hops import Amarillo, Simcoe
from brew.shbf import AmericanPaleAle
from brew.yeast import LibertyBellAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "FolkAPA"
        self.style = AmericanPaleAle()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(1.25),
            MunichI(1.0),
            WheatMalt(0.25),
            GoldenSyrup(0.25)
        ]
        self.hops = [Simcoe(15, 15), Amarillo(10, 15), Amarillo(15, 0)]
        self.yeast = LibertyBellAle()
        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

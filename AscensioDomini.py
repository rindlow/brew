#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    PaleAleMalt,
    WhiteSugar
)
from brew.hops import Perle, Saaz
from brew.shbf import Tripel
from brew.yeast import TrappistHighGravity


class Recipe(brew.Recipe):
    def __init__(self):
        self.style = Tripel()
        self.profile = Braumeister20l()
        self.fermentables = [
            PaleAleMalt(6),
            WhiteSugar(1.0)
        ]
        self.hops = [
            Saaz(30, 60),
            Perle(10, 60),
            Saaz(30, 30),
            Perle(10, 30)
        ]
        self.yeast = TrappistHighGravity()
        self.boil_time = 60
        self.batch_size = 17
        self.mash = brew.SingleStepMashWithMashOut(65)


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

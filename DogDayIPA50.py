#!/usr/bin/env python

import brew
from brew.profiles import Braumeister50l
from brew.fermentables import (
    Pilsen6RW,
    MarisOtterAleMalt,
    WhiteSugar,
    CaraGold,
)
from brew.hops import Ekuanot, Simcoe
from brew.shbf import AmericanIPA
from brew.yeast import US05


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Dog Day IPA"
        self.style = AmericanIPA()
        self.description = "East Coast IPA"
        self.profile = Braumeister50l()
        self.fermentables = [
            MarisOtterAleMalt(7.0),
            CaraGold(3.6),
            Pilsen6RW(2.4),
            WhiteSugar(1.0),
        ]
        self.hops = [
            Simcoe(45, 60),
            Simcoe(50, 10),
            Ekuanot(50, 10),
            Simcoe(90, 0),
            Ekuanot(90, 0),
            Simcoe(100, brew.dryhop),
            Ekuanot(150, brew.dryhop),
        ]
        self.yeast = US05()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 44


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    CaraHell,
    WheatMalt,
)
from brew.hops import HallertauerMittelfruh
from brew.shbf import Kolsch
from brew.yeast import K97


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Mittelfrüh"
        self.style = Kolsch()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(4.5),
            CaraHell(0.25),
            WheatMalt(0.25),
        ]
        self.hops = [
            HallertauerMittelfruh(55, 50, alpha=3.7),
            HallertauerMittelfruh(30, 0, alpha=3.7),
        ]
        self.yeast = K97()
        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

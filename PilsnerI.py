#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    DextrinMalt,
    PilsnerMalt,
    GoldenSyrup,
)
from brew.hops import (
    Saaz,
    NorthernBrewer
)
from brew.shbf import CzechPilsener
from brew.yeast import BohemianLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Pilsner"
        self.style = CzechPilsener()
        self.profile = Braumeister20l()
        self.fermentables = [
            PilsnerMalt(5.0),
            DextrinMalt(0.5),
            GoldenSyrup(0.15),
        ]
        self.hops = [
            Saaz(30, 60, alpha=3.3),
            NorthernBrewer(8, 60, alpha=12.2),
            Saaz(20, 40, alpha=3.3),
            Saaz(30, 20, alpha=3.3),
        ]  # 30.3
        self.yeast = BohemianLager()
        self.mash = brew.SingleStepMash(68)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.log(
        brew_date="2020-01-26",
        original_gravity=1.053,
        racking_date="2020-03-07",
        final_gravity=1.015,
    )
    recipe.log(
        brew_date="2022-10-27",
        original_gravity=1.047,
        racking_date="2022-11-10",
        final_gravity=1.010,
    )
    recipe.run()

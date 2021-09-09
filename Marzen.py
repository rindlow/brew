#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    Pilsen6RW,
    CaraGold,
    MunichI,
    WhiteSugar,
)
from brew.hops import Saaz
import brew.shbf
from brew.yeast import BavarianLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Märzen"
        self.style = brew.shbf.Marzen()
        self.profile = Braumeister20l()
        self.fermentables = [
            Pilsen6RW(1.7),
            MunichI(3.0),
            CaraGold(1.3),
            WhiteSugar(0.25),
        ]
        self.hops = [Saaz(55, 60), Saaz(15, 15)]
        self.yeast = BavarianLager()
        self.mash = brew.MashSchedule(
            [
                brew.Step(67, 60, "Saccharification rest"),
                brew.Step(77, 10, "Mash Out"),
            ]
        )
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2019-04-28",
        original_gravity=1.053,
        racking_date="2019-05-14",
        final_gravity=1.015,
    )

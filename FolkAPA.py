#!/usr/bin/env python

from brew import Recipe, SingleStepMash
from brew.fermentables import (
    GoldenSyrup,
    MarisOtterAleMalt,
    MunichI,
    WheatMalt,
)
from brew.hops import Amarillo
from brew.profiles import Braumeister20l
from brew.shbf import AmericanPaleAle
from brew.yeast import LibertyBellAle


class Recipe(Recipe):
    def __init__(self) -> None:
        self.name = "FolkAPA"
        self.style = AmericanPaleAle()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(1.25),
            MunichI(1.0),
            WheatMalt(0.25),
            GoldenSyrup(0.25),
        ]
        self.hops = [
            Amarillo(5, 60, alpha=9.6),
            Amarillo(25, 15, alpha=9.6),
            Amarillo(25, 0, alpha=9.6),
        ]
        self.yeast = LibertyBellAle()
        self.mash = SingleStepMash(67)

        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.log(
        brew_date="2026-04-26",
        original_gravity=1.028,
        racking_date="2026-05-26",
        final_gravity=1.008,
    )
    recipe.run()

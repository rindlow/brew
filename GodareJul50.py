#!/usr/bin/env python

import brew
from brew.profiles import Braumeister50l
from brew.fermentables import (
    PaleAleMalt,
    Aromatic,
    BiscuitMalt,
    Crystal240,
    SpecialB,
    ChocolateMalt,
    CandiSyrup,
    WhiteSugar,
)
from brew.hops import Perle, Saaz
from brew.shbf import DarkStrongBelgianAle
from brew.yeast import BelgianAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Godare Jul"
        self.style = DarkStrongBelgianAle()
        self.style_override = "9K"
        self.description = "An elegant and warming Christmas ale"
        self.profile = Braumeister50l()
        self.fermentables = [
            PaleAleMalt(9.0),
            Aromatic(2.0),
            BiscuitMalt(0.5),
            Crystal240(0.5),
            SpecialB(0.5),
            ChocolateMalt(0.5),
            CandiSyrup(2.5),
            WhiteSugar(1.0),
        ]
        self.hops = [
            Perle(50, 40, alpha=7.0),
            Perle(50, 30, alpha=7.0),
            Saaz(50, 20),
            Saaz(50, 10),
        ]
        self.other = [
            brew.Ingredient("Coriander seeds", "25 g", "in boil"),
            brew.Ingredient("Bitter Orange peel", "40 g", "in boil"),
        ]
        self.yeast = BelgianAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 45


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
#     recipe.log(
#         brew_date="2018-09-29",
#         original_gravity=1.076,
#         racking_date="2018-10-13",
#         final_gravity=1.01,
#     )

#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
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
        self.profile = Braumeister20l()
        self.fermentables = [
            PaleAleMalt(4.0),
            Aromatic(1.0),
            BiscuitMalt(0.25),
            Crystal240(0.25),
            SpecialB(0.25),
            ChocolateMalt(0.25),
            CandiSyrup(1.0),
            WhiteSugar(0.5),
        ]
        self.hops = [
            Perle(20, 40, alpha=7.0),
            Perle(20, 30, alpha=7.0),
            Saaz(20, 20),
            Saaz(20, 10),
        ]
        self.other = [
            brew.Ingredient("Coriander seeds", "10 g", "in boil"),
            brew.Ingredient("Bitter Orange peel", "15 g", "in boil"),
        ]
        self.yeast = BelgianAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 18


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    recipe.log(
        brew_date="2018-09-29",
        original_gravity=1.076,
        racking_date="2018-10-13",
        final_gravity=1.01,
    )

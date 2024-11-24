#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    CaraRuby,
    Crystal100,
    MelanoidinMalt,
    ViennaMalt,
    WheatMalt,
)
from brew.hops import (
    HallertauerMittelfruh,
    BavariaMandarina,
)
import brew.shbf
from brew.yeast import SouthernGermanLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Rotbier"
        self.description = "Nürnberger Rotbier"
        self.style = brew.shbf.FranconianLager()
        self.profile = Braumeister20l()
        self.fermentables = [
            CaraRuby(0.8),
            MelanoidinMalt(0.4),
            ViennaMalt(1.6),
            Crystal100(0.5),
            WheatMalt(0.1),
        ]
        self.hops = [
            BavariaMandarina(15, 60, alpha=7.4),
            HallertauerMittelfruh(20, 10, alpha=3.4),
            BavariaMandarina(20, 10, alpha=7.4)]
        self.yeast = SouthernGermanLager()
        self.mash = brew.SingleStepMash(68)

        self.boil_time = 60
        self.batch_size = 17


if __name__ == "__main__":
    recipe = Recipe()
    recipe.log(
        brew_date="2024-05-25",
        original_gravity=1.034,
        racking_date="2024-06-08",
        final_gravity=1.011,
    )
    recipe.run()

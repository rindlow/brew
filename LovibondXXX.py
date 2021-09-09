#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import AshburneMildMalt
from brew.hops import Cluster, EastKentGoldings
from brew.shbf import EnglishIPA
from brew.yeast import WhitbreadAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "1864 Lovibond XXXX"
        self.style = EnglishIPA()
        self.description = "Mild"
        self.profile = Braumeister20l()
        self.fermentables = [
            AshburneMildMalt(6.0)
        ]
        self.hops = [
            Cluster(20, 60),
            EastKentGoldings(20, 30),
            EastKentGoldings(20, 15),
        ]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(64)
        self.boil_time = 60
        self.batch_size = 14


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

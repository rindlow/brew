#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    FlakedMaize,
    WhiteSugar
)
from brew.hops import (
    Willamette,
    EastKentGoldings,
    Cluster
)
from brew.shbf import EnglishIPA
from brew.yeast import WestYorkshireAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "1910 Warwicks IPA"
        self.style = EnglishIPA()
        self.description = "English IPA"
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(4.0),
            FlakedMaize(1.4),
            WhiteSugar(0.7),
        ]
        self.hops = [
            Cluster(40, 60),
            Willamette(40, 30),
            EastKentGoldings(60, brew.dryhop),
        ]
        self.yeast = WestYorkshireAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    PaleAleMalt,
    AshburneMildMalt,
    Crystal150,
    AmberMalt,
    FlakedMaize,
    WhiteSugar,
    Caramel,
)
from brew.hops import Fuggle
from brew.shbf import EnglishBestBitter
from brew.yeast import WhitbreadAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "XX"
        self.style = EnglishBestBitter()
        self.style_override = "3G"
        self.profile = Braumeister20l()
        self.description = [
            "Clone of Barklay Perkins XX from 1935.",
            "http://barclayperkins.blogspot.com/2017/09/"
            "lets-brew-wednesday-1935-barclay.html",
        ]
        self.fermentables = [
            AshburneMildMalt(2.0),
            PaleAleMalt(1.0),
            Crystal150(0.3),
            AmberMalt(0.3),
            FlakedMaize(0.8),
            WhiteSugar(0.2),
            Caramel(0.01),
        ]
        self.hops = [Fuggle(25, 60), Fuggle(14, 30)]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

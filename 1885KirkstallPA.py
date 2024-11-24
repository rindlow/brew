#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    MarisOtterAleMalt,
    GoldenSyrup,
)
from brew.hops import EastKentGoldings, HallertauerMittelfruh
from brew.shbf import EnglishIPA
from brew.yeast import WhitbreadAle


class Recipe(brew.Recipe):
    """https://barclayperkins.blogspot.com/2022/10/lets-brew-wednesday-1885-kirkstall-pa.html"""
    
    def __init__(self):
        self.name = "1885 Kirkstall PA"
        self.style = EnglishIPA()
        self.profile = Braumeister20l()
        self.fermentables = [
            MarisOtterAleMalt(6),
            GoldenSyrup(0.6),
        ]
        self.hops = [
            HallertauerMittelfruh(50, 60),
            EastKentGoldings(50, 60),
            EastKentGoldings(30, 30)]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()
    # recipe.log(
    #     brew_date="2019-01-06",
    #     original_gravity=1.074,
    #     racking_date="2019-02-21",
    #     final_gravity=1.014,
    # )

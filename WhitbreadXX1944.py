#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    AshburneMildMalt,
    Crystal150,
    GoldenSyrup,
    FlakedBarley,
    Caramel,
)
from brew.hops import (
    Fuggle,
    Cluster
)
from brew.shbf import EnglishDarkMild
from brew.yeast import WhitbreadAle


class Recipe(brew.Recipe):
    """http://barclayperkins.blogspot.com/2019/09/\
lets-brew-wednesday-1944-whitbread-xx_18.html"""

    def __init__(self):
        self.name = "1944 Whitbread XX"
        self.style = EnglishDarkMild()
        self.description = "Mild"
        self.profile = Braumeister20l()
        self.fermentables = [
            AshburneMildMalt(2.2),
            Crystal150(0.25),
            FlakedBarley(0.5),
            GoldenSyrup(0.125),
            Caramel(0.01),
        ]
        self.hops = [
            Cluster(3, 60),
            Fuggle(10, 60),
            Fuggle(15, 30)
        ]
        self.yeast = WhitbreadAle()
        self.mash = brew.SingleStepMashWithMashOut(64)
        self.boil_time = 60
        self.batch_size = 20


if __name__ == "__main__":
    recipe = Recipe()
    recipe.run()

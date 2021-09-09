#!/usr/bin/env python

import brew
from brew.fermentables import (
    PaleAleMalt,
    MunichI,
    CaraMunichI
)
from brew.hops import (
    Cascade,
    Amarillo
)
from brew.profiles import Braumeister20l
from brew.shbf import AmericanIPA
from brew.yeast import LibertyBellAle


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Brewed On The 4th Of July"
        self.description = "American Red IPA"
        self.style = AmericanIPA()
        self.profile = Braumeister20l()
        self.fermentables = [
            PaleAleMalt(4.0),
            MunichI(1.0),
            CaraMunichI(1.0)
        ]
        self.hops = [
            Cascade(10, 60, alpha=9.0),
            Amarillo(15, 60, alpha=7.9),
            Cascade(20, 15, alpha=9.0),
            Amarillo(25, 10, alpha=7.9),
            Cascade(30, 5, alpha=9.0),
            Cascade(40, 1, alpha=9.0),
            Amarillo(40, 0, alpha=7.9),
        ]
        self.yeast = LibertyBellAle()
        self.mash = brew.SingleStepMashWithMashOut(67)
        self.boil_time = 60
        self.batch_size = 15


recipe = Recipe()
recipe.run()
recipe.log(
    brew_date="2018-07-04",
    original_gravity=1.06,
    racking_date="2018-07-18",
    final_gravity=1.018,
)

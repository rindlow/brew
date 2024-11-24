#!/usr/bin/env python

import brew
from brew.profiles import Braumeister20l
from brew.fermentables import (
    ChocolateMalt,
    DarkMunich,
    WhiteSugar,
)
from brew.hops import HallertauerMittelfruh
import brew.shbf
from brew.yeast import BavarianLager


class Recipe(brew.Recipe):
    def __init__(self):
        self.name = "Kulmbacher Export"
        self.style = brew.shbf.Marzen()
        self.style_override = '2E'
        self.profile = Braumeister20l()
        self.fermentables = [
            DarkMunich(5.8),
            ChocolateMalt(0.2),
            WhiteSugar(0.4),
        ]
        self.hops = [
            HallertauerMittelfruh(70, 60, alpha=3.7),
            HallertauerMittelfruh(70, 30, alpha=3.7)]
        self.yeast = BavarianLager()
        self.mash = brew.SingleStepMashWithMashOut(67)

        self.boil_time = 60
        self.batch_size = 17


if __name__ == "__main__":
    recipe = Recipe()
    recipe.log(
        brew_date="2022-04-18",
        original_gravity=1.063,
        racking_date="2022-05-28",
        final_gravity=1.019,
    )
    recipe.log(
        brew_date="2023-10-15",
        original_gravity=1.061,
        racking_date="2023-10-29",
        final_gravity=1.018,
    )
    recipe.run()

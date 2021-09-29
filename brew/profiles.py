class Profile:

    max_boil_volume = 0.0
    min_mash_volume = 0.0
    max_mash_volume = 0.0
    max_malt_weight = 0.0
    mash_efficiency = 0.
    water_in_malt_ratio = 0.0
    kettle_deadspace = 0.0
    power = 0.0
    boil_off_rate = 0.0


class Braumeister20l(Profile):

    max_boil_volume = 30.0
    min_mash_volume = 16.0
    max_mash_volume = 25.0
    max_malt_weight = 6.0
    mash_efficiency = 0.82
    water_in_malt_ratio = 1.0
    kettle_deadspace = 4.0
    power = 2000 * 0.75
    boil_off_rate = 2.0


class Braumeister50l(Profile):

    max_boil_volume = 60.0
    min_mash_volume = 40.0
    max_mash_volume = 55.0
    max_malt_weight = 13.0
    mash_efficiency = 0.82
    water_in_malt_ratio = 1.0
    kettle_deadspace = 4.0
    power = 3400 * 0.75
    boil_off_rate = 4.0

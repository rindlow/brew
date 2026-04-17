class Profile:
    max_boil_volume: float = 0.0
    min_batch_size: float = 0.0
    max_mash_volume: float = 0.0
    max_malt_weight: float = 0.0
    mash_efficiency: float = 0.0
    water_in_malt_ratio: float = 0.0
    kettle_deadspace: float = 0.0
    power: float = 0.0
    boil_off_rate: float = 0.0


class Braumeister20l(Profile):
    max_boil_volume = 30.0
    min_batch_size = 16.0
    max_mash_volume = 25.0
    max_malt_weight = 6.0
    mash_efficiency = 0.82
    water_in_malt_ratio = 1.0
    kettle_deadspace = 4.0
    power = 2000 * 0.75
    boil_off_rate = 2.0


class Braumeister50l(Profile):
    max_boil_volume = 60.0
    min_batch_size = 40.0
    max_mash_volume = 55.0
    max_malt_weight = 13.0
    mash_efficiency = 0.82
    water_in_malt_ratio = 1.0
    kettle_deadspace = 4.0
    power = 3400 * 0.75
    boil_off_rate = 4.0

from config.meal_nutrient_ratio import CARBS_RATIO, FAT_RATIO, PROTEIN_RATIO


def init_nutrient(prefix: str = ''):
    obj = {}
    obj[prefix + "kcal"] = 0
    obj[prefix + "protein"] = 0
    obj[prefix + "fat"] = 0
    obj[prefix + "carbs"] = 0
    return obj


def add_nutrient(_object, nutrient, object_prefix='', nutrient_prefix=''):
    _object[object_prefix+"kcal"] += getattr(nutrient, f"{nutrient_prefix}kcal")
    _object[object_prefix+"protein"] += getattr(nutrient, f"{nutrient_prefix}protein")
    _object[object_prefix+"fat"] += getattr(nutrient, f"{nutrient_prefix}fat")
    _object[object_prefix+"carbs"] += getattr(nutrient, f"{nutrient_prefix}carbs")


def subtract_nutrietn(_object, nutrient, object_prefix='', nutrient_prefix=''):
    _object[object_prefix+"kcal"] -= getattr(nutrient, f"{nutrient_prefix}kcal")
    _object[object_prefix+"protein"] -= getattr(nutrient, f"{nutrient_prefix}protein")
    _object[object_prefix+"fat"] -= getattr(nutrient, f"{nutrient_prefix}fat")
    _object[object_prefix+"carbs"] -= getattr(nutrient, f"{nutrient_prefix}carbs")


def make_min_max_nutrient(kcal):
    min_nutrient = init_nutrient()
    max_nutrient = init_nutrient()
    min_nutrient["kcal"] = kcal
    max_nutrient["kcal"] = kcal + 100

    min_nutrient["carbs"] = round((min_nutrient["kcal"] * CARBS_RATIO) / 4)
    max_nutrient["carbs"] = round((max_nutrient["kcal"] * CARBS_RATIO) / 4)

    min_nutrient["protein"] = round((min_nutrient["kcal"] * PROTEIN_RATIO) / 4)
    max_nutrient["protein"] = round((max_nutrient["kcal"] * PROTEIN_RATIO) / 4)

    min_nutrient["fat"] = round((min_nutrient["kcal"] * FAT_RATIO) / 9)
    max_nutrient["fat"] = round((max_nutrient["kcal"] * FAT_RATIO) / 9)

    return min_nutrient, max_nutrient

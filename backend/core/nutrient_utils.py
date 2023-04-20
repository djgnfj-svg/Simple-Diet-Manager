

def init_nutrient(_object, prefix: str = ''):
    _object[prefix + "kcal"] = 0
    _object[prefix + "protein"] = 0
    _object[prefix + "fat"] = 0
    _object[prefix + "carbs"] = 0


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
    # 비율은 탄단지 = 45 : 40 : 15
    min_nutrient = {}
    max_nutrient = {}
    init_nutrient(min_nutrient)
    init_nutrient(max_nutrient)
    min_nutrient["kcal"] = kcal
    max_nutrient["kcal"] = kcal + 100

    min_nutrient["carbs"] = round((min_nutrient["kcal"] * 0.45) / 4)
    max_nutrient["carbs"] = round((max_nutrient["kcal"] * 0.45) / 4)

    min_nutrient["protein"] = round((min_nutrient["kcal"] * 0.4) / 4)
    max_nutrient["protein"] = round((max_nutrient["kcal"] * 0.4) / 4)

    min_nutrient["fat"] = round((min_nutrient["kcal"] * 0.15) / 9)
    max_nutrient["fat"] = round((max_nutrient["kcal"] * 0.15) / 9)

    return min_nutrient, max_nutrient

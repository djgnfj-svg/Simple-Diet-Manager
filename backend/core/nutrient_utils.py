from config.meal_nutrient_ratio import CARBS_RATIO, FAT_RATIO, PROTEIN_RATIO

def cal_range(value, range):
    return round(value * range)

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

def cal_nutrient_range(metabolic, range):
    nutrient = {}
    nutrient["kcal"] = cal_range(metabolic["kcal"], range)
    nutrient["carbs"] = cal_range(metabolic["carbs"], range)
    nutrient["protein"] = cal_range(metabolic["protein"], range)
    nutrient["fat"] = cal_range(metabolic["fat"], range)
    return nutrient

def get_min_max_range(diet_status):
    '''
    감량 : 0,
    유지 : 1,
    증량 : 2
    '''

    if diet_status == 0:
        return 0.8, 0.9
    elif diet_status == 1:
        return 0.9, 1.0
        
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

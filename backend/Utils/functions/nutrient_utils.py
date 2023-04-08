

def init_nutrient(_object, prefix:str=None):
    if prefix is None:
        _object["kcal"] = 0
        _object["protein"] = 0
        _object["fat"] = 0
        _object["carbs"] = 0
    else:
        _object[prefix + "kcal"] = 0
        _object[prefix + "protein"] = 0
        _object[prefix + "fat"] = 0
        _object[prefix + "carbs"] = 0

def add_nutrietn(_object, food, prefix:str=None):
    if prefix is None:
        _object["kcal"] += food.kcal
        _object["protein"] += food.protein
        _object["fat"] += food.fat
        _object["carbs"] += food.carbs
    else:
        _object[prefix + "kcal"] += food.kcal
        _object[prefix + "protein"] += food.protein
        _object[prefix + "fat"] += food.fat
        _object[prefix + "carbs"] += food.carbs

def minus_nutrietn(_object, food, prefix:str=None):
    if prefix is None:
        _object["kcal"] -= food.kcal
        _object["protein"] -= food.protein
        _object["fat"] -= food.fat
        _object["carbs"] -= food.carbs
    else:
        _object[prefix + "kcal"] -= food.kcal
        _object[prefix + "protein"] -= food.protein
        _object[prefix + "fat"] -= food.fat
        _object[prefix + "carbs"] -= food.carbs

def make_nutrient(kcal):
    # 비율은 탄단지 = 45 : 40 : 15
    # return min_nutrient, max_nutrient
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

    
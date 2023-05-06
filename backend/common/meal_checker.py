from foods.models import Food


class MealChecker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check_nutrient(min_nutrient, nutrient, nutrient_name, prefix=None):
        if min_nutrient[nutrient_name] <= nutrient[prefix + nutrient_name]:
            return True
        else:
            return False

    @staticmethod
    def check_all_nutrient(min, max, obj, prefix=None):
        if min["kcal"] <= obj[prefix+"kcal"] <= max["kcal"] and \
                min["protein"] <= obj[prefix+"protein"] <= max["protein"] and \
                min["fat"] <= obj[prefix+"fat"] <= max["fat"] and \
                min["carbs"] <= obj[prefix+"carbs"] <= max["carbs"]:
            return True
        else:
            return False

    @staticmethod
    def over_nutrient_limit(_cn, max_nutrient, nutrient_name, food: Food, prefix=None):
        if _cn[prefix + nutrient_name] + getattr(food, nutrient_name) > max_nutrient[nutrient_name]:
            return True
        else:
            return False
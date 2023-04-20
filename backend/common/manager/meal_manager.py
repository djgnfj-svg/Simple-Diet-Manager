from common.manager.base_manager import DietManagerBase
from core.nutrient_utils import (add_nutrient, init_nutrient,
                                 make_min_max_nutrient)
from foods.models import Food
from meals.models import Meal


class MealChecker:
    def __init__(self) -> None:
        pass

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
    def check_nutirent(min_nutrient, max_nutrient, nutrient, nutrient_name, prefix=None):
        if min_nutrient[nutrient_name] <= nutrient[prefix + nutrient_name]:
            return True
        else:
            return False

    @staticmethod
    def check_food_over_nutrient(nutrient, max_nutrient, nutrient_name, food:Food, prefix=None):
        if nutrient[prefix + nutrient_name] + getattr(food, nutrient_name) > max_nutrient[nutrient_name]:
            return True
        else:
            return False
    
class MealManager(DietManagerBase):
    # TODO : 요일 받기 6/3 해가 지고 남머지로 식단 추출하면됨 어짜피 삼시새끼로 할꺼니까
    def get_data(self, need_nutrient, min_range, max_range):
        min_range -= 0.1

        min_nutrient, max_nutrient = make_min_max_nutrient(need_nutrient["need_kcal"])
        meal = self.find_instance(Meal, "meal_", min_nutrient, max_nutrient)

        if meal.count() > 2:
            return meal[0]
        else :
            return self.make_instance(min_nutrient, max_nutrient)

    def make_instance(self, min_nutrient, max_nutrient, _food:Food=None):
        # TODO : 일단 임시 방편...
        min_nutrient["protein"] *= 0.5
        min_nutrient["fat"] *= 0.5
        min_nutrient["carbs"] *= 0.5
        
        current_nutrient = {}
        food_list = []

        init_nutrient(current_nutrient, prefix="current_")
        if _food:
            food_list.append(_food)
            add_nutrient(current_nutrient, _food, "current_")


        nutrient = ["kcal", "protein", "fat", "carbs"]
        nutrient_focus = 1
        food_focus = 0

        while nutrient_focus < 4:
            # 현재 영양소를 만족했는가?
            if  MealChecker.check_nutirent(min_nutrient, max_nutrient, current_nutrient, nutrient[nutrient_focus], prefix="current_"):
                nutrient_focus += 1
                food_focus = 0
                continue

            # 현재 영양소가 가장 큰 음식을 가져온다.
            food = Food.objects.order_by("-" + nutrient[nutrient_focus])[food_focus]

            # 그것을 추가할때 max nutrient를 오버한다면 다음식품으로 넘아간다.
            if MealChecker.check_food_over_nutrient(current_nutrient, max_nutrient, nutrient[nutrient_focus], food, prefix="current_"):
                food_focus += 1
                continue

            add_nutrient(current_nutrient, food, "current_")
            food_list.append(food)
            food_focus += 1
                
        meal = Meal.objects.create(
            meal_kcal= current_nutrient["current_kcal"],
            meal_protein= current_nutrient["current_protein"],
            meal_fat= current_nutrient["current_fat"],
            meal_carbs= current_nutrient["current_carbs"],
        )
        meal.foods.set(food_list)
        meal.save()
        return meal

    def meke_meal_range(self,start, stop, step,food:Food = None):
        for kcal in range(start, stop, step):
            min, max = make_min_max_nutrient(kcal)
            self.make_instance(min, max, food)
from django.db.models import Q

from diets.models import Diet

from meals.MealManager import MealManager

from Utils.common.ManagerBase import ManagerBase
from Utils.functions.nutrient_utils import init_nutrient
from Utils.nutrient.Nutrient import NutrientCalculator as nc


class DietManager(ManagerBase):
    def __init__(self, meal_count):
        self.data = {}

        if meal_count == 1:
            self.__meals = ["breakfast"]
            self.__meals_nutrient = [1]
        elif meal_count == 2:
            self.__meals = ["breakfast", "lunch"]
            self.__meals_nutrient = [0.6, 0.4]
        elif meal_count == 3:
            self.__meals = ["breakfast", "lunch", "dinner"]
            self.__meals_nutrient = [0.4, 0.3, 0.3]

    # TODO : Make 함수를 만들어서 if 부분을 읽기 쉽게
    def get_data(self, metabolic_data, min_range, max_range):
        init_nutrient(self.data, prefix="diet_")
        min_nutrient, max_nutrient =  self._cal_nutirient(metabolic_data, min_range, max_range)

        q = Q()
        q &= Q(diet_kcal__gte=min_nutrient["kcal"], diet_kcal__lte=max_nutrient["kcal"])
        q &= Q(diet_protein__gte=min_nutrient["protein"], diet_protein__lte=max_nutrient["protein"])
        q &= Q(diet_fat__gte=min_nutrient["fat"], diet_fat__lte=max_nutrient["fat"])
        q &= Q(diet_carbs__gte=min_nutrient["carbs"], diet_carbs__lte=max_nutrient["carbs"])

        diet = Diet.objects.filter(q)

        if diet.count() > 0:
            return diet[0]
        else :
            meal_list = []
            meal_data = {}
            init_nutrient(meal_data, prefix="diet_")

            for _, nutrient_range in zip(self.__meals, self.__meals_nutrient):
                need_nutrient = {}
                need_nutrient["need_kcal"] = metabolic_data["metabolism_kcal"] * nutrient_range
                need_nutrient["need_protein"] = metabolic_data["metabolism_protein"] * nutrient_range
                need_nutrient["need_fat"] = metabolic_data["metabolism_fat"] * nutrient_range
                need_nutrient["need_carbs"] = metabolic_data["metabolism_carbs"] * nutrient_range
                
                meal_manager = MealManager()
                _meal = meal_manager.get_data(need_nutrient, min_range, max_range)
                meal_list.append(_meal)
                
                meal_data["diet_kcal"] += _meal.meal_kcal
                meal_data["diet_protein"] += _meal.meal_protein
                meal_data["diet_fat"] += _meal.meal_fat
                meal_data["diet_carbs"] += _meal.meal_carbs

        diet = Diet.objects.create(
            diet_kcal=meal_data["diet_kcal"],
            diet_protein=meal_data["diet_protein"],
            diet_fat=meal_data["diet_fat"],
            diet_carbs=meal_data["diet_carbs"],
        )
        diet.meals.set(meal_list)
        return diet
    
    @staticmethod
    def _cal_nutirient(metabolic_data, min_range, max_range):
        min_nutrient = {}
        min_nutrient["kcal"] = nc.cal_range(metabolic_data["metabolism_kcal"], min_range)
        min_nutrient["carbs"] = nc.cal_range(metabolic_data["metabolism_carbs"], min_range)
        min_nutrient["protein"] = nc.cal_range(metabolic_data["metabolism_protein"], min_range)
        min_nutrient["fat"] = nc.cal_range(metabolic_data["metabolism_fat"], min_range)

        max_nutrient = {}
        max_nutrient["kcal"] = nc.cal_range(metabolic_data["metabolism_kcal"], max_range)
        max_nutrient["carbs"] = nc.cal_range(metabolic_data["metabolism_carbs"], max_range)
        max_nutrient["protein"] = nc.cal_range(metabolic_data["metabolism_protein"], max_range)
        max_nutrient["fat"] = nc.cal_range(metabolic_data["metabolism_fat"], max_range)

        return min_nutrient, max_nutrient
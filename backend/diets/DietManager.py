from Utils.common.ManagerBase import ManagerBase
from Utils.functions.nutrient_utils import init_nutrient
from meals.MealManager import MealManager


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


    def get_data(self, metabolic_data, meal_option, min_range, max_range):
        meal_manager = MealManager()
        init_nutrient(self.data, prefix="total_")
        for meal, nutrient_range in zip(self.__meals, self.__meals_nutrient):
            need_nutrient = {}
            need_nutrient["need_kcal"] = metabolic_data["metabolism_kcal"] * nutrient_range
            need_nutrient["need_protein"] = metabolic_data["metabolism_protein"] * nutrient_range
            need_nutrient["need_fat"] = metabolic_data["metabolism_fat"] * nutrient_range
            need_nutrient["need_carbs"] = metabolic_data["metabolism_carbs"] * nutrient_range
            
            self.data[meal] = meal_manager.get_data(need_nutrient, meal_option, min_range, max_range)
            self.data["total_kcal"] += self.data[meal]["meal_kcal"]
            self.data["total_protein"] += self.data[meal]["meal_protein"]
            self.data["total_fat"] += self.data[meal]["meal_fat"]
            self.data["total_carbs"] += self.data[meal]["meal_carbs"]
        return self.data
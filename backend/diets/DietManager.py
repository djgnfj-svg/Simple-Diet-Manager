from Utils.common.ManagerBase import ManagerBase
from meals.MealManager import Meal_Manager


class DietManager(ManagerBase):
    def __init__(self):
        self.data = {}

    def get_data(self, metabolic_data, meal_option, meal_count, min_range, max_range):
        if meal_count == 1:
            meals = ["breakfast"]
            meals_nutrient = [1]
        elif meal_count == 2:
            meals = ["breakfast", "lunch"]
            meals_nutrient = [0.6, 0.4]
        elif meal_count == 3:
            meals = ["breakfast", "lunch", "dinner"]
            meals_nutrient = [0.4, 0.3, 0.3]

        meal_manager = Meal_Manager()
        self.data["total_kcal"] = 0
        self.data["total_protein"] = 0
        self.data["total_fat"] = 0
        self.data["total_carbs"] = 0
        for meal, nutrient_range in zip(meals, meals_nutrient):
            need_nutrient = {}
            need_nutrient["kcal"] = metabolic_data["total_kcal"] * nutrient_range
            need_nutrient["protein"] = metabolic_data["total_protein"] * nutrient_range
            need_nutrient["fat"] = metabolic_data["total_fat"] * nutrient_range
            need_nutrient["carbs"] = metabolic_data["total_carbs"] * nutrient_range
            
            self.data[meal] = meal_manager.get_data(need_nutrient, meal_option, min_range, max_range)
            self.data["total_kcal"] += self.data[meal]["meal_kcal"]
            self.data["total_protein"] += self.data[meal]["meal_protein"]
            self.data["total_fat"] += self.data[meal]["meal_fat"]
            self.data["total_carbs"] += self.data[meal]["meal_carbs"]
        return self.data
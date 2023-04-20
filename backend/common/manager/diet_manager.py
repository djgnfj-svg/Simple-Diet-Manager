from common.manager.base_manager import DietManagerBase
from common.manager.meal_manager import MealManager
from core.nutrient import NutrientCalculator as nc
from core.nutrient_utils import add_nutrient, init_nutrient
from diets.models import Diet


# TODO : 중복검사 만들어야 한다.
class DietManager(DietManagerBase):
    def __init__(self, meal_count):
        if meal_count == 1:
            self.__meals = ["breakfast"]
            self.__meals_nutrient = [1]
        elif meal_count == 2:
            self.__meals = ["breakfast", "lunch"]
            self.__meals_nutrient = [0.6, 0.4]
        elif meal_count == 3:
            self.__meals = ["breakfast", "lunch", "dinner"]
            self.__meals_nutrient = [0.4, 0.3, 0.3]

    def get_data(self, metabolic_data, min_range, max_range):
        min_nutrient, max_nutrient =  self._cal_nutirient(metabolic_data, min_range, max_range)
        diet = self.find_instance(Diet, "diet_", min_nutrient, max_nutrient)
        if diet.count() > 0:
            return diet[0]
        else :
            return self.make_instance(metabolic_data, min_range, max_range)
    
    def make_instance(self, metabolic_data, min_range, max_range):
        diet_data = {}
        meal_list = []
        init_nutrient(diet_data)

        for _, nutrient_range in zip(self.__meals, self.__meals_nutrient):
            need_nutrient = {}
            need_nutrient["need_kcal"] = metabolic_data["metabolism_kcal"] * nutrient_range
            need_nutrient["need_protein"] = metabolic_data["metabolism_protein"] * nutrient_range
            need_nutrient["need_fat"] = metabolic_data["metabolism_fat"] * nutrient_range
            need_nutrient["need_carbs"] = metabolic_data["metabolism_carbs"] * nutrient_range
            
            meal_manager = MealManager()
            _meal = meal_manager.get_data(need_nutrient, min_range, max_range)
            add_nutrient(diet_data, _meal, nutrient_prefix="meal_")
            meal_list.append(_meal)

        diet = Diet.objects.create(
            diet_kcal=diet_data["kcal"],
            diet_protein=diet_data["protein"],
            diet_fat=diet_data["fat"],
            diet_carbs=diet_data["carbs"],
        )
        diet.meals.set(meal_list)
        return diet

    # TODO : 이것도 부모 클래스로 올려서 * 6 하는 느낌으로 해도 되겠다.
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
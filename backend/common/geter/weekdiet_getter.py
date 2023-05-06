from common.geter.base_getter import GetterBase

from accounts.models import UserBodyInfo
from common.maker.weekdiet_maker import WeekDietMaker
from core.nutrient import NutrientCalculator as nc
from diets.models import WeekDiet


class WeekDietGetter(GetterBase):
    def __init__(self):
        pass

    def get_data(self, meal_count, userbody: UserBodyInfo, metabolic, min_range, max_range):
        min_nutrient, max_nutrient = self._cal_week_nutirient(metabolic, min_range, max_range)
        week_diet = self.find_instance(WeekDiet, "week_", min_nutrient, max_nutrient, meal_count)

        # TODO : 0번째인지는 미정이다.
        if week_diet.count() > 0:
            return week_diet[0] 
        else :
            return WeekDietMaker.make_instance(meal_count, metabolic, min_range, max_range, userbody)

    def _cal_week_nutirient(self, metabolic_data, min_range, max_range):
        min_week_nutrient = {}
        min_week_nutrient["kcal"] = nc.cal_range(metabolic_data["metabolism_kcal"], min_range) * 6
        min_week_nutrient["carbs"] = nc.cal_range(metabolic_data["metabolism_carbs"], min_range) * 6
        min_week_nutrient["protein"] = nc.cal_range(metabolic_data["metabolism_protein"], min_range) * 6
        min_week_nutrient["fat"] = nc.cal_range(metabolic_data["metabolism_fat"], min_range) * 6

        max_week_nutrient = {}
        max_week_nutrient["kcal"] = nc.cal_range(metabolic_data["metabolism_kcal"], max_range) * 6
        max_week_nutrient["carbs"] = nc.cal_range(metabolic_data["metabolism_carbs"], max_range) * 6
        max_week_nutrient["protein"] = nc.cal_range(metabolic_data["metabolism_protein"], max_range) * 6
        max_week_nutrient["fat"] = nc.cal_range(metabolic_data["metabolism_fat"], max_range) * 6

        return min_week_nutrient, max_week_nutrient

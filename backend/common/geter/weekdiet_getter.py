from core.nutrient_utils import cal_nutrient_range
from common.geter.base_getter import GetterBase

from common.maker.weekdiet_maker import WeekDietMaker
from diets.models import WeekDiet


class WeekDietGetter(GetterBase):
    def __init__(self):
        pass

    def get_data(self, meal_count, userbody, min_nutrient, max_nutrient, categories):
        week_min_nutrient = cal_nutrient_range(min_nutrient, 6)
        week_max_nutrient = cal_nutrient_range(max_nutrient, 6)
        
        week_diet = self.find_instance(WeekDiet, week_min_nutrient, week_max_nutrient, meal_count, categories)

        # TODO : 0번째인지는 미정이다.
        if week_diet.count() > 0:
            return week_diet[0] 
        else :
            week_maker = WeekDietMaker(WeekDiet)
            return week_maker.make_instance(meal_count, min_nutrient, max_nutrient, userbody, categories)


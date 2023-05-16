from common.geter.base_getter import GetterBase
from common.maker.meal_maker import MealMaker

from core.nutrient_utils import make_min_max_nutrient


class MealGetter(GetterBase):
    def __init__(self, _model):
        super().__init__(_model)
    
    def get_data(self, need_nutrient, category):
        min_nutrient, max_nutrient = make_min_max_nutrient(need_nutrient["need_kcal"])
        meal = self.find_instance(self.model, min_nutrient, max_nutrient, category=category)

        if meal.exists():
            return meal[0]
        else :
            make_manager = MealMaker(self.model)
            return make_manager.make_instance(min_nutrient, max_nutrient)
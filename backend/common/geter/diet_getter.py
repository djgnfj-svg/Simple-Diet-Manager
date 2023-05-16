from core.nutrient_utils import cal_range
from common.maker.diet_maker import DietMaker
from common.geter.base_getter import GetterBase
from diets.models import Diet


class DietGetter(GetterBase):
    def __init__(self, model, meal_count):
        super().__init__(model)
        self.maker = DietMaker(model, meal_count)

    #TODO : 추후 옵션으로 월 화 수 각자 다르게 할 수 있도록
    def get_data(self, min_nutrient, max_nutrient, meal_count, category):
        
        diet = self.find_instance(Diet, min_nutrient, max_nutrient, meal_count, category)
        if diet.count() > 0:
            return diet.first()
        else :
            return self.maker.make_instance(min_nutrient, meal_count, category)
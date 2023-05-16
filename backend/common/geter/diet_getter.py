from common.maker.diet_maker import DietMaker
from common.geter.base_getter import GetterBase
from core.nutrient import NutrientCalculator as nc
from diets.models import Diet


class DietGetter(GetterBase):
    def __init__(self, model, meal_count):
        super().__init__(model)
        self.maker = DietMaker(model, meal_count)

    #TODO : 추후 옵션으로 월 화 수 각자 다르게 할 수 있도록
    def get_data(self, metabolic_data, min_range, max_range, meal_count):
        min_nutrient, max_nutrient =  self._cal_nutirient(metabolic_data, min_range, max_range)
        
        diet = self.find_instance(Diet, min_nutrient, max_nutrient, meal_count)
        if diet.count() > 0:
            return diet[0]
        else :
            return self.maker.make_instance(metabolic_data, min_range, max_range, meal_count)

    # TODO : 이것도 부모 클래스로 올려서 * 6 하는 느낌으로 해도 되겠다.
    @staticmethod
    def _cal_nutirient(metabolic_data, min_range, max_range):
        min_nutrient = {}
        min_nutrient["kcal"] = nc.cal_range(metabolic_data["kcal"], min_range)
        min_nutrient["carbs"] = nc.cal_range(metabolic_data["carbs"], min_range)
        min_nutrient["protein"] = nc.cal_range(metabolic_data["protein"], min_range)
        min_nutrient["fat"] = nc.cal_range(metabolic_data["fat"], min_range)

        max_nutrient = {}
        max_nutrient["kcal"] = nc.cal_range(metabolic_data["kcal"], max_range)
        max_nutrient["carbs"] = nc.cal_range(metabolic_data["carbs"], max_range)
        max_nutrient["protein"] = nc.cal_range(metabolic_data["protein"], max_range)
        max_nutrient["fat"] = nc.cal_range(metabolic_data["fat"], max_range)

        return min_nutrient, max_nutrient
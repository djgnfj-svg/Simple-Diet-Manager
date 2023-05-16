from django.db import transaction

from common.geter.meal_getter import MealGetter
from common.maker.base_maker import MakerBase
from config.meal_nutrient_ratio import ONE_MEAL_NUTRIENT, THREE_MEAL_NUTRIENT, TWO_MEAL_NUTRIENT

from core.nutrient_utils import add_nutrient, init_nutrient
from meals.models import Meal


class DietMaker(MakerBase):
    def __init__(self, _model, meal_count):
        super().__init__(_model)
        if meal_count == 1:
            self.__meals = ["breakfast"]
            self.__meals_nutrient = ONE_MEAL_NUTRIENT
        elif meal_count == 2:
            self.__meals = ["breakfast", "lunch"]
            self.__meals_nutrient = TWO_MEAL_NUTRIENT
        elif meal_count == 3:
            self.__meals = ["breakfast", "lunch", "dinner"]
            self.__meals_nutrient = THREE_MEAL_NUTRIENT

    @transaction.atomic
    def make_instance(self, min_nutrient, meal_count, category, bulk=False):
        diet_data = init_nutrient()
        meal_list = []
        
        for _, nutrient_range in zip(self.__meals, self.__meals_nutrient):
            need_nutrient = {}
            need_nutrient["need_kcal"] = min_nutrient["kcal"] * nutrient_range
            need_nutrient["need_protein"] = min_nutrient["protein"] * nutrient_range
            need_nutrient["need_fat"] = min_nutrient["fat"] * nutrient_range
            need_nutrient["need_carbs"] = min_nutrient["carbs"] * nutrient_range
            
            meal_getter = MealGetter(Meal)
            _meal = meal_getter.get_data(need_nutrient, category)
            add_nutrient(diet_data, _meal)
            meal_list.append(_meal)

        if bulk:
            return diet_data
        
        # TODO : 추후 base class로 올려서 1큐로 해결하자
        # if self.model.objects.filter(meals__in=meal_list, meal_count=meal_count).exists():
        #     diet = self.model.objects.filter(meals__in=meal_list, meal_count=meal_count).first()
        else :
            diet = self.model.objects.create(
                kcal=diet_data["kcal"],
                protein=diet_data["protein"],
                fat=diet_data["fat"],
                carbs=diet_data["carbs"],
                meal_count = meal_count
            )
            diet.meals.set(meal_list)
            diet.save()
        return diet
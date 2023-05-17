from django.db import transaction
from diets.models import Diet
from common.geter.diet_getter import DietGetter

from common.maker.base_maker import MakerBase
from core.nutrient_utils import add_nutrient, init_nutrient


class WeekDietMaker(MakerBase):
    def __init__(self, model):
        super().__init__(model)

    @transaction.atomic
    def make_instance(self, meal_count, min_nutrient, max_nutrient, userbody, categories):
        week_nutrient_data = init_nutrient()
        diet_list = []
        
        #카테고리 1,2,3로 반복한다
        for category in categories:
            diet_manger = DietGetter(Diet, meal_count)
            _diet = diet_manger.get_data(min_nutrient, max_nutrient, meal_count, category)
            # 2번 더하는게 맞다
            add_nutrient(week_nutrient_data, _diet)
            add_nutrient(week_nutrient_data, _diet)
            diet_list.append(_diet)
        diet_list = diet_list * 2

        # 추후 쿼리계산해서 1개로 줄이자
        if self.model.objects.filter(diets__in=diet_list, meal_count=meal_count).exists() and \
            len(self.model.objects.filter(diets__in=diet_list, meal_count=meal_count).first().diets.all()) == len(diet_list):
            return self.model.objects.filter(diets__in=diet_list, meal_count=meal_count).first()
        
        week_diet = self.model.objects.create(
            kcal=week_nutrient_data["kcal"],
            protein=week_nutrient_data["protein"],
            fat=week_nutrient_data["fat"],
            carbs=week_nutrient_data["carbs"],
            meal_count = meal_count,
            bodyinfo=userbody,
        )
        week_diet.diets.set(diet_list)

        return week_diet
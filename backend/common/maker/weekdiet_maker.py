from django.db import transaction
from diets.models import Diet
from common.geter.diet_getter import DietGetter

from common.maker.base_maker import MakerBase
from core.nutrient_utils import add_nutrient, init_nutrient


class WeekDietMaker(MakerBase):
    def __init__(self, model):
        super().__init__(model)

    @transaction.atomic
    def make_instance(self, meal_count, metabolic, min_range, max_range, userbody):
        week_nutrient_data = init_nutrient()
        diet_list = []
        
        # 월화수 를만들어서 목금토로 복사하기 때문에  주간식단 6일치가 나온다.
        for i in range(0,3):
            diet_manger = DietGetter(Diet, meal_count)
            _diet = diet_manger.get_data(metabolic, min_range, max_range, meal_count)
            # 2번 더하는게 맞다
            add_nutrient(week_nutrient_data, _diet, nutrient_prefix="diet_")
            add_nutrient(week_nutrient_data, _diet, nutrient_prefix="diet_")
            diet_list.append(_diet)
        diet_list = diet_list * 2

        # 추후 쿼리계산해서 1개로 줄이자
        if self.model.objects.filter(diets__in=diet_list, meal_count=meal_count).exists():
            return self.model.objects.filter(diets__in=diet_list, meal_count=meal_count).first()

        week_diet = self.model.objects.create(
            week_kcal=week_nutrient_data["kcal"],
            week_protein=week_nutrient_data["protein"],
            week_fat=week_nutrient_data["fat"],
            week_carbs=week_nutrient_data["carbs"],
            meal_count = meal_count,
            bodyinfo=userbody,
        )
        week_diet.diets.set(diet_list)

        return week_diet
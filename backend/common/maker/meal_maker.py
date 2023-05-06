from django.db import transaction
from common.maker.base_maker import MakerBase
from common.meal_checker import MealChecker as checker

from core.nutrient_utils import add_nutrient, init_nutrient, make_min_max_nutrient
from foods.models import Food
from meals.models import Meal


class MealMaker(MakerBase):
    def __init__(self, model) -> None:
        super().__init__(model)
        self.nutrient = ["kcal", "protein", "fat", "carbs"]

    @transaction.atomic
    def make_instance(self, min_nutrient, max_nutrient, _food: Food = None, bulk_create: bool = False):
        # TODO : 일단 임시 방편...
        min_nutrient["protein"] *= 0.5
        min_nutrient["fat"] *= 0.5
        min_nutrient["carbs"] *= 0.5

        # current_nutrient
        cn = init_nutrient(prefix="current_")
        food_list = []

        if _food:
            food_list.append(_food)
            add_nutrient(cn, _food, object_prefix="current_")

        #nutrient focus
        nf = 1
        food_focus = 0

        qs_food = Food.objects.order_by("-" + self.nutrient[nf])
        while nf < len(self.nutrient):
            if checker.check_nutrient(min_nutrient, cn, self.nutrient[nf], prefix="current_"):
                nf += 1
                if nf < len(self.nutrient):
                    break
                else:
                    food_focus = 0
                    qs_food = Food.objects.order_by("-" + self.nutrient[nf])
                continue

            food = qs_food[food_focus]
            if checker.over_nutrient_limit(cn, max_nutrient, self.nutrient[nf], food, prefix="current_"):
                food_focus += 1
                continue

            add_nutrient(cn, food, "current_")
            food_list.append(food)
            food_focus += 1

        if bulk_create:
            return cn

        if self.model.objects.filter(foods__in=food_list).exists():
            meal = self.model.objects.filter(foods__in=food_list).first()
        else:
            meal = Meal.objects.create(
                meal_kcal=cn["current_kcal"],
                meal_protein=cn["current_protein"],
                meal_fat=cn["current_fat"],
                meal_carbs=cn["current_carbs"],
            )
            meal.foods.set(food_list)
            meal.save()
        return meal

    def meke_meal_range(self, start, stop, step, food: Food = None, bulk_create=False):
        meal_list = []
        for kcal in range(start, stop, step):
            min_nutrient, max_nutrient = make_min_max_nutrient(kcal)
            nutrient = self.make_instance(min_nutrient, max_nutrient, food, bulk_create=bulk_create)
            meal_list.append(
                Meal(
                    meal_kcal=nutrient["current_kcal"],
                    meal_protein=nutrient["current_protein"],
                    meal_fat=nutrient["current_fat"],
                    meal_carbs=nutrient["current_carbs"],
                )
            )
        if bulk_create:
            Meal.objects.bulk_create(meal_list)

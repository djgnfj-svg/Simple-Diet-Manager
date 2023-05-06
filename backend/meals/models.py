from typing import Any
from django.db import models

from common.models import TimeStampedModel
from foods.models import Food


class MealManager(models.Manager):
    def meal_create(self, foods, meal_count, **kwargs: Any) -> Any:
        meal = self.filter(foods__in=foods).first()
        if meal != None and len(meal.foods.all()) == len(foods):
            return meal
        else :
            meal = super().create(**kwargs)

            meal.foods.set(foods)
            meal.meal_count = meal_count
            meal.meal_kcal=meal.foods.aggregate(models.Sum("kcal")).get("kcal__sum")
            meal.meal_protein=meal.foods.aggregate(models.Sum("protein")).get("protein__sum")
            meal.meal_fat=meal.foods.aggregate(models.Sum("fat")).get("fat__sum")
            meal.meal_carbs=meal.foods.aggregate(models.Sum("carbs")).get("carbs__sum")
            meal.meal_img=meal.foods.order_by("-protein").first().img
            meal.name=f'{meal.foods.order_by("-protein").first().name} 외 {meal.foods.count() -1}개'
        return meal


class Meal(TimeStampedModel):
    name = models.CharField(max_length=50, null=True, blank=True)

    foods = models.ManyToManyField(Food, related_name="meals")
    meal_kcal = models.IntegerField(null=False, default=0)
    meal_protein = models.IntegerField(null=False, default=0)
    meal_fat = models.IntegerField(null=False, default=0)
    meal_carbs = models.IntegerField(null=False, default=0)
    meal_video = models.URLField(max_length=100, null=True, blank=True)
    meal_img = models.ImageField(upload_to='meal/%Y/%m/%d/', null=True, blank=True)
    meal_count = models.IntegerField(null=False, default=3)
    objects = MealManager()

    class meta:
        db_table = "meal"

    def save(self, *args, **kwargs):
        if self.id :
            if self.foods.count() == 1:
                self.name = self.foods.first().name
            else :
                self.name = f'{self.foods.order_by("-protein").first().name} 외 {self.foods.count() -1}개'
        else :
            self.name = "새로운 식단 | 아직 음식 없음"
        return super().save(*args, **kwargs)
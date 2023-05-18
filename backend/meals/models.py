from typing import Any

from django.db import models

from common.models import TimeStampedModel
from foods.models import Food, FoodCategory


class MealManager(models.Manager):
    def meal_update(self, foods, category,  **kwargs: Any) -> Any:
        meal = self.filter(foods__in=foods).first()
        if meal == None or len(meal.foods.all()) != len(foods):
            meal.foods.clear()
            meal.foods.set(foods)
            meal.kcal=meal.foods.aggregate(models.Sum("kcal")).get("kcal__sum")
            meal.protein=meal.foods.aggregate(models.Sum("protein")).get("protein__sum")
            meal.fat=meal.foods.aggregate(models.Sum("fat")).get("fat__sum")
            meal.carbs=meal.foods.aggregate(models.Sum("carbs")).get("carbs__sum")
            meal.image=meal.foods.order_by("-protein").first().image
            meal.name=f'{meal.foods.order_by("-protein").first().name} 외 {meal.foods.count() -1}개'
            meal.save()
            return meal
        else :
            raise ValueError("이미 존재하는 식사입니다.")

    def meal_create(self, foods, category, **kwargs: Any) -> Any:
        meal = self.filter(foods__in=foods).first()
        if meal != None and len(meal.foods.all()) == len(foods):
            return meal
        else :
            kwargs["category"] = category
            meal = super().create(**kwargs)

            meal.foods.set(foods)
            meal.kcal=meal.foods.aggregate(models.Sum("kcal")).get("kcal__sum")
            meal.protein=meal.foods.aggregate(models.Sum("protein")).get("protein__sum")
            meal.fat=meal.foods.aggregate(models.Sum("fat")).get("fat__sum")
            meal.carbs=meal.foods.aggregate(models.Sum("carbs")).get("carbs__sum")
            meal.image=meal.foods.order_by("-protein").first().image
            meal.name=f'{meal.foods.order_by("-protein").first().name} 외 {meal.foods.count() -1}개'
            meal.category = category
        return meal


class Meal(TimeStampedModel):
    foods = models.ManyToManyField(Food, related_name="meals")
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="meals")
    name = models.CharField(max_length=50, null=True, blank=True)

    kcal = models.IntegerField(null=False, default=0)
    protein = models.IntegerField(null=False, default=0)
    fat = models.IntegerField(null=False, default=0)
    carbs = models.IntegerField(null=False, default=0)

    image = models.ImageField(upload_to='meal/%Y/%m/%d/', null=True, blank=True)

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
from django.db import models

from accounts.models import UserBodyInfo
from foods.models import FoodCategory
from meals.models import Meal

from common.models import TimeStampedModel


# class DietManager(models.Manager):
#     def diet_create(self, meals, )

class Diet(TimeStampedModel):
    meals = models.ManyToManyField(Meal)
    # category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)

    meal_count = models.IntegerField(default=0)

class WeekDiet(TimeStampedModel):
    diets = models.ManyToManyField(Diet)
    bodyinfo = models.ForeignKey(UserBodyInfo, on_delete=models.CASCADE)
    # categories = models.ManyToManyField(FoodCategory)

    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    
    meal_count = models.IntegerField(default=0)

class MultiURL(models.Model):
    url = models.CharField(max_length=200)
    WeekDiet = models.ForeignKey(WeekDiet, on_delete=models.CASCADE)
from django.db import models

from accounts.models import User
from common.models import TimeStampedModel
from foods.models import FoodCategory
from meals.models import Meal

# class DietManager(models.Manager):
#     def diet_create(self, meals, )

class Diet(TimeStampedModel):
    meals = models.ManyToManyField(Meal)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)

    meal_count = models.IntegerField(default=0)

class WeekDiet(TimeStampedModel):
    diets = models.ManyToManyField(Diet)
    categories = models.ManyToManyField(FoodCategory)

    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    
    meal_count = models.IntegerField(default=0)
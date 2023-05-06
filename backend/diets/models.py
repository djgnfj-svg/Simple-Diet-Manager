from django.db import models

from accounts.models import UserBodyInfo
from meals.models import Meal


class Diet(models.Model):
    meals = models.ManyToManyField(Meal, related_name="days")

    diet_kcal = models.IntegerField(default=0)
    diet_protein = models.IntegerField(default=0)
    diet_fat = models.IntegerField(default=0)
    diet_carbs = models.IntegerField(default=0)
    meal_count = models.IntegerField(default=0)

class WeekDiet(models.Model):
    diets = models.ManyToManyField(Diet, related_name="weeks")
    
    bodyinfo = models.ForeignKey(UserBodyInfo, on_delete=models.CASCADE, related_name="weeks")
    week_kcal = models.IntegerField(default=0)
    week_protein = models.IntegerField(default=0)
    week_fat = models.IntegerField(default=0)
    week_carbs = models.IntegerField(default=0)
    meal_count = models.IntegerField(default=0)
from django.db import models

from accounts.models import BodyInfoRecord

from meal.models import Meal

# Create your models here.

class DietOption(models.Model):
    options = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class WeekDiet(models.Model):
    diet_option = models.ForeignKey(DietOption, on_delete=models.CASCADE, related_name="weeks")
    BodyInfo = models.ForeignKey( BodyInfoRecord, on_delete=models.CASCADE, related_name="weeks")
    created_at = models.DateTimeField(auto_now_add=True)

class Diet(models.Model):
    diet_option = models.ForeignKey(DietOption, on_delete=models.CASCADE, related_name="days")
    week_diet = models.ForeignKey(WeekDiet, on_delete=models.CASCADE, related_name="days")

    meals = models.ManyToManyField(Meal, related_name="days")

    day_of_week = models.CharField(max_length=50)
    total_kcal = models.IntegerField(default=0)
    tital_protein = models.IntegerField(default=0)
    total_fat = models.IntegerField(default=0)
    total_carbs = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

from food.models import Food

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=50)

    foods = models.ManyToManyField(Food, related_name="meals")
    meal_kcal = models.IntegerField()
    meal_protein = models.IntegerField()
    meal_fat = models.IntegerField()
    meal_carbs = models.IntegerField()
    meal_video = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
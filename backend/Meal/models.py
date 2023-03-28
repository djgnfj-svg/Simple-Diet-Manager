from django.db import models

from food.models import Food

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=50)

    foods = models.ManyToManyField(Food, related_name="meals")
    total_kcal = models.IntegerField()
    tital_protein = models.IntegerField()
    total_fat = models.IntegerField()
    total_carbs = models.IntegerField()
    meal_video = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
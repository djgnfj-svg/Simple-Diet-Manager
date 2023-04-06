from django.db import models

from foods.models import Food
    
class Meal(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    foods = models.ManyToManyField(Food, related_name="meals")
    meal_kcal = models.IntegerField(null=False, default=0)
    meal_protein = models.IntegerField(null=False, default=0)
    meal_fat = models.IntegerField(null=False, default=0)
    meal_carbs = models.IntegerField(null=False, default=0)
    meal_video = models.URLField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = "meal"

    def __str__(self) -> str:
        return self.name
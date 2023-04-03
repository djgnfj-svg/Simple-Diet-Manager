from django.db import models

from food.models import Food
    
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

    def save(self, isupdate=False, foods=None) -> None:
        if isupdate:
            self.meal_kcal = 0
            self.meal_protein = 0
            self.meal_fat = 0
            self.meal_carbs = 0

        for food in foods:
            self.meal_kcal += food.kcal
            self.meal_protein += food.protein
            self.meal_fat += food.fat
            self.meal_carbs += food.carbs

        if len(foods.all()) > 1:
            self.name = f"{foods[0].name}  외 {len(foods.all())-1}개"
        else:
            self.name = f"{foods[0].name}"

        return super().save()
    
    def __str__(self) -> str:
        return self.name
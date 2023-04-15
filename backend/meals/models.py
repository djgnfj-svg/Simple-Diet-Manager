from django.db import models
from foods.models import FoodCategory

from foods.models import Food
    
from Utils.model.Timestemp import TimeStampedModel


class Meal(TimeStampedModel):
    name = models.CharField(max_length=50, null=True, blank=True)

    foods = models.ManyToManyField(Food, related_name="meals")
    meal_kcal = models.IntegerField(null=False, default=0)
    meal_protein = models.IntegerField(null=False, default=0)
    meal_fat = models.IntegerField(null=False, default=0)
    meal_carbs = models.IntegerField(null=False, default=0)
    meal_video = models.URLField(max_length=100, null=True, blank=True)
    meal_img = models.ImageField(upload_to='meal/%Y/%m/%d/', null=True, blank=True)

    class meta:
        db_table = "meal"

    def save(self, *args, **kwargs):
        if self.id :
            self.meal_img = self.foods.order_by("-protein").first().img
            name = FoodCategory.objects.get(id = self.foods.order_by("-protein").first().category_id).name
            self.name = f'{name} 외 {self.foods.count() - 1}개'
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
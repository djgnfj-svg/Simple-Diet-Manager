from django.db import models

from common.models import TimeStampedModel
from foods.models import Food, FoodCategory


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
            # TODO : 음식의 종류가 3개 이하이면 음식의 카테고리를 모두 써주자 겹치는개 있다면 숫자로 표시 (닭가슴살 2, 요거트 1) 이런씩으로 
            self.name = f'{name} 외 {self.foods.count() - 1}개'
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
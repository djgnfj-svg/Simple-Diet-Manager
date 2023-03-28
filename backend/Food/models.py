from django.db import models

from Utils.model.Timestemp import TimeStampedModel

# Create your models here.
class FoodCategory(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

class CookingOption(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)


class Food(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    kcal = models.IntegerField(null=False, default=0)
    protein = models.IntegerField(null=False, default=0)
    fat = models.IntegerField(null=False, default=0)
    carbs = models.IntegerField(null=False, default=0)

    number = models.IntegerField(null=False, default=0)
    gram = models.IntegerField(null=False, default=0)
    link = models.URLField(max_length=100, null=True)
    img = models.ImageField(upload_to='food_img')

    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="foods")
    cooking = models.ForeignKey(CookingOption, on_delete=models.CASCADE, related_name="foods")
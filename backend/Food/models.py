from django.db import models

from Utils.model.Timestemp import TimeStampedModel

# Create your models here.
class FoodCategory(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class CookingOption(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
    


class Food(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    kcal = models.IntegerField(null=False, default=0)
    protein = models.IntegerField(null=False, default=0)
    fat = models.IntegerField(null=False, default=0)
    carbs = models.IntegerField(null=False, default=0)

    number = models.IntegerField(null=False, default=0)
    gram = models.IntegerField(null=False, default=0)
    iscoupangfresh = models.BooleanField(default=False)
    link = models.URLField(max_length=100, null=True)
    img = models.ImageField(upload_to='food_img')

    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="foods")
    cookingoption = models.ForeignKey(CookingOption, on_delete=models.CASCADE, related_name="foods")

    def __str__(self) -> str:
        return f"{self.name} : kcal : {self.kcal}, protein : {self.protein}, fat : {self.fat}, carbs : {self.carbs}"
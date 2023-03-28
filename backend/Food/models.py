from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    name = models.CharField(max_length=50)


class Food(models.Model):
    name = models.CharField(max_length=50)
    kcal = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()

    food_count = models.IntegerField()
    food_link = models.URLField(max_length=100)
    food_img = models.ImageField(upload_to='food_img')
    created_at = models.DateTimeField(auto_now_add=True)
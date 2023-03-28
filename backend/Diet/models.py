from django.db import models

# Create your models here.

class Week_Diet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class Day_Diet(models.Model):
    week_diet = models.ForeignKey(Week_Diet, on_delete=models.CASCADE, related_name="days")
    total_kcal = models.IntegerField()
    tital_protein = models.IntegerField()
    total_fat = models.IntegerField()
    total_carbs = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
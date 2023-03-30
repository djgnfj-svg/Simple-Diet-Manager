from django.contrib import admin
from food.models import CookingOption, Food, FoodCategory


# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(CookingOption)
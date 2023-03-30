from django import forms
from django.contrib import admin
from food.models import Food

from meal.models import Meal
# Register your models here.


class MealAdmin(admin.ModelAdmin):
    readonly_fields = ('meal_kcal', 'meal_protein', 'meal_fat', 'meal_carbs')
    def save_model(self, request, obj, form, change) -> None:
        if obj.id:
            return obj.save(isupdate=True, foods=form.cleaned_data['foods'])
        return obj.save(foods=form.cleaned_data['foods'])
    
admin.site.register(Meal, MealAdmin)
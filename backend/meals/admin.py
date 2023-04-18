from django.contrib import admin

from meals.models import Meal

# Register your models here.


# class MealAdmin(admin.ModelAdmin):
#     readonly_fields = ('meal_kcal', 'meal_protein', 'meal_fat', 'meal_carbs')
#     def save_model(self, request, obj, form, change) -> None:
#         return obj.save(isupdate=change, foods=form.cleaned_data['foods'])
    
admin.site.register(Meal)

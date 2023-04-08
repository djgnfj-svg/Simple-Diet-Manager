
from django.apps import AppConfig




class MealsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meals'

    def ready(self):
        from meals.models import Meal
        from meals.MealManager import MealMakeManager

        if Meal.objects.count() == 0:
            makemanager = MealMakeManager()
            makemanager.meke_meal_range(300, 1200, 100)
from django.apps import AppConfig
from django.core.management import call_command


class MealsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meals'

    # def ready(self):
    #     call_command('migrate', '--noinput')
    #     from foods.models import Food

    #     if Food.objects.count() > 20:
        
    #         from common.manager.meal_manager import MealManager
    #         from meals.models import Meal
        
    #         if Meal.objects.count() == 0:
    #             for food in Food.objects.all():
    #                 makemanager = MealManager()
    #                 makemanager.meke_meal_range(300, 1200, 100, food)

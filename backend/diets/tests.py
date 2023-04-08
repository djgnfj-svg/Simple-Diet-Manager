import itertools
from django.test import TestCase
from Utils.Metabolic.MetabolicManager import MetabolicManager
from Utils.functions.nutrient_utils import make_nutrient
from foods.models import Food
from meals.MealManager import MealMakeManager
from meals.models import Meal
from diets.DietManager import DietManager

from diets.WeekDietManager import WeekDietManager

# Create your tests here.


class WeekDietMakeTest(TestCase):
    fixtures = ['_Master_data/Foods.json', '_Master_data/Food-Category.json', '_Master_data/Cooking-Category.json']
    def setUp(self):
        self.data = {
            'age': 25, 
            'weight': 80, 
            'height': 173, 
            'gender': 'M', 
            'general_activity': 1.2, 
            'excise_activity': 0.2, 
            'iscoupangfresh': True, 
            'meal_count': 3, 
            'diet_status': 1
        }

        if Meal.objects.count() == 0:
            makemanager = MealMakeManager()
            makemanager.meke_meal_range(300, 1200, 100,)
        self.week_diet_manager = WeekDietManager()
        self.diet_manager = DietManager(self.data['meal_count'])
        pass

    def test_week_diet(self):
        week_diet_data = self.week_diet_manager.get_data(self.data)
        self.assertIn('mon', week_diet_data)
        self.assertIn('tue', week_diet_data)
        self.assertIn('wed', week_diet_data)
        self.assertIn('thu', week_diet_data)
        self.assertIn('fri', week_diet_data)
        self.assertIn('sat', week_diet_data)
        self.assertIn('sun', week_diet_data)
        pass

    def test_diet_make(self):
        metabolic_manager = MetabolicManager()
        metabolic_data = metabolic_manager.get_data(self.data)
        min_range = 0.5 if self.data['diet_status'] else 0.9
        max_range = 0.9 if self.data['diet_status'] else 1

        diet_data = self.diet_manager.get_data(metabolic_data, min_range, max_range)
        self.assertIn('breakfast', diet_data)
        self.assertIn('lunch', diet_data)
        self.assertIn('dinner', diet_data)

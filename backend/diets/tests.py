from django.test import TestCase

from Utils.Metabolic.MetabolicManager import MetabolicManager

from accounts.models import UserBodyInfo

from meals.MealManager import MealMakeManager
from meals.models import Meal

from diets.models import WeekDiet, Diet
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
        userbodyinfo = UserBodyInfo.objects.create(
            age=self.data['age'],
            weight=self.data['weight'],
            height=self.data['height'],
            gender = self.data['gender'],
            general = self.data['general_activity'],
            activity = self.data['excise_activity'],
        )
        metabolic_manager = MetabolicManager()
        metabolic = metabolic_manager.get_data(self.data)
        week_diet_data = self.week_diet_manager.get_data(self.data["meal_count"]\
            , userbodyinfo, metabolic=metabolic,min_range=0.8, max_range=0.9)
        
        self.assertEqual(type(week_diet_data), WeekDiet)
        pass

    def test_diet_make(self):
        metabolic_manager = MetabolicManager()
        metabolic_data = metabolic_manager.get_data(self.data)
        min_range = 0.5 if self.data['diet_status'] else 0.9
        max_range = 0.9 if self.data['diet_status'] else 1

        diet_data = self.diet_manager.get_data(metabolic_data, min_range, max_range)
        self.assertEqual(type(diet_data), Diet)

from django.test import TestCase

from accounts.models import UserBodyInfo
from common.manager.diet_manager import DietManager
from common.manager.meal_manager import MealManager
from common.manager.weekdiet_manager import WeekDietManager
from core.metabolic_manager import MetabolicManager
from diets.models import Diet, WeekDiet
from foods.models import Food
from meals.models import Meal


# Create your tests here.
class DietTest(TestCase):
    fixtures = ['_Master_data/Foods.json', '_Master_data/Food-Category.json', '_Master_data/Cooking-Category.json']
    def setUp(self) -> None:
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
            makemanager = MealManager()
            makemanager.meke_meal_range(300, 1200, 100, bulk_create=True)
        self.week_diet_manager = WeekDietManager()
        self.diet_manager = DietManager(self.data['meal_count'])
    
    #중복 생성 방지
    def test_duplicate_fail(self):
        diet1 = Diet.objects.create(
            diet_kcal = 1000,
            diet_protein = 100,
            diet_fat = 100,
            diet_carbs = 100,
        )
        diet1.meals.set(Meal.objects.all()[:3])
        diet2 = Diet.objects.create(
            diet_kcal = 1000,
            diet_protein = 100,
            diet_fat = 100,
            diet_carbs = 100,
        )
        diet2.meals.set(Meal.objects.all()[:3])
        # self.assertEqual(Diet.objects.count(), 1)


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
            makemanager = MealManager()
            makemanager.meke_meal_range(300, 1200, 100,bulk_create=True)
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
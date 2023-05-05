from django.db import connection
from django.test import TestCase
from backend.meals.models import Meal

from foods.models import Food


class MealManagerTest(TestCase):
    fixtures = ['_Master_data/Foods.json', '_Master_data/Food-Category.json', '_Master_data/Cooking-Category.json']

    def setUp(self):
        self.food = Food.objects.get(id=1)
from django.test import TestCase
from foods.models import Food

from foods.FoodManager import FoodManager

# Create your tests here.
class FoodManagerTest(TestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Cooking-Category.json', '_Master_data/Foods.json']
    def setUp(self):
        self.food_manager = FoodManager()

    def test_get_food(self):
        food = self.food_manager.get_data("protein", 0)
        self.assertEqual(type(food), Food)


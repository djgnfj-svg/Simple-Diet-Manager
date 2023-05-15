# 모델테스트
'''
초과 미만 없음
'''

from django.test import TestCase
from meals.models import Meal

class MealTest(TestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']
    
    def test_meal_create(self):
        meal = Meal.objects.meal_create(foods=[1,2,3])

        self.assertEqual(meal.id, 1)
        self.assertGreaterEqual(meal.meal_kcal, 3)
        self.assertGreaterEqual(meal.meal_protein, 3)
        self.assertGreaterEqual(meal.meal_fat, 3)
        self.assertGreaterEqual(meal.meal_carbs, 3)
        self.assertGreaterEqual(len(meal.name), 3)
    
    def test_meal_create_duplicate(self):
        meal = Meal.objects.meal_create(foods=[1,2,3])
        meal2 = Meal.objects.meal_create(foods=[1,2,3])

        self.assertEqual(Meal.objects.count(), 1)

    def test_meal_create_list_in_but_not_duplicate(self):
        meal = Meal.objects.meal_create(foods=[1,2,3])
        meal2 = Meal.objects.meal_create(foods=[1,2,3, 4])
        self.assertEqual(Meal.objects.count(), 2)
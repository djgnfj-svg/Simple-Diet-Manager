from django.test import TestCase
from foods.models import Food
from django.db import connection

class MealManagerTest(TestCase):
    fixtures = ['_Master_data/Foods.json', '_Master_data/Food-Category.json', '_Master_data/Cooking-Category.json']
    def test_meal_manager(self):
        connection.queries.clear() # 쿼리 로그를 초기화합니다.

        for food in Food.objects.all():
            print(food.category.name)

        print("첫 번째 반복문에서 실행된 쿼리 수: ", len(connection.queries))

        connection.queries.clear() # 쿼리 로그를 초기화합니다.

        for food in Food.objects.all().select_related('category'):
            print(food.category.name)

        print("두 번째 반복문에서 실행된 쿼리 수: ", len(connection.queries))

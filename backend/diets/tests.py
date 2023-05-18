# 모델테스트
'''
초과 미만 없음
'''

from django.test import TestCase

from diets.models import Diet, WeekDiet


# 
class DietTest(TestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']
    def setUp(self) -> None:
        return super().setUp()
    

class WeekDietTest(TestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']
    def setUp(self) -> None:
        return super().setUp()
    


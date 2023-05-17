# API테스트
'''
생성
삭제
수정
조회

실패
초과 미만 없음
'''

from rest_framework.test import APITestCase
import random

class DietAPITest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']
    
    def setUp(self):
        self.url = '/api/week-diets/'

    def generate_random_data(self):
        data = {
            "age": random.randint(20, 60),
            "weight": random.randint(50, 130),
            "height": random.randint(158, 200),
            "gender": random.choice(["M", "W"]),
            "general_activity": random.choice(["1.2", "1.4", "1.6"]),
            "excise_activity": random.choice(["0.0", "0.1", "0.2"]),
            "meal_count": random.choice([2, 3]),
            "diet_status": random.choice([0, 1]),
            "categories": random.sample([1, 2, 3, 4, 5], 3)
        }
        return data
    
    def test_weekdiet_create(self):
        for _ in range(50):
            data = self.generate_random_data()
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, 201)
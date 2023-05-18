from rest_framework.test import APITestCase
import random

from diets.models import WeekDiet

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
        for _ in range(25):
            data = self.generate_random_data()
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, 201)
            for diet in WeekDiet.objects.order_by("created_at").last().diets.all():
                self.assertEqual(diet.meal_count, data["meal_count"])

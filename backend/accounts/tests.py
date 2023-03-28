from django.test import TestCase
from rest_framework import status
# Create your tests here.

class DietTest(TestCase):
    def setUp(self) -> None:
        self.url = '/api/diets/'
        self.sample_data = {
            'age': 20,
            'weight': 80,
            'height': 170,
            'gender': 'M',
            'general_activities': 1.2,
            'excise_activity': 0.2,

            'meal_count' : 3,
        }

        return super().setUp()
    def test_diet(self):
        response = self.client.post(self.url, self.sample_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
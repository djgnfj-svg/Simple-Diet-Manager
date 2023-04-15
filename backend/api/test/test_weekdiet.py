from rest_framework.test import APITestCase


class FoodAddTest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json',
                '_Master_data/Cooking-Category.json', '_Master_data/Foods.json']

    def setUp(self) -> None:
        self.url = '/api/week-diets/'

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

    def test_status_week_diet(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 201)

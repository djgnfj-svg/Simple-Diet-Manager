from rest_framework.test import APITestCase

#  make test DRF food add api


class FoodAddTest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json',
                '_Master_data/Cooking-Category.json']

    def setUp(self) -> None:
        self.url = '/api/foods/'
        self.food_data = {
            "name": "한끼통살 통살 닭가슴살 허니소이",
            "kcal": 135,
            "protein": 21,
            "fat": 12,
            "carbs": 9,
            "number": 10,
            "gram": 100,
            "link": "https://www.coupang.com/vp/products/6081081115?itemId=11273250763",
            "category": 1,
            "cookingoption": 5,
        }
        return super().setUp()

    def test_food_add(self):
        response = self.client.post(self.url, self.food_data, format='json')
        self.assertEqual(response.status_code, 201)

from rest_framework.test import APITestCase

#  make test DRF food add api
class FoodAddTest(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/foods/'
        self.food_data = {
            "name": "한끼통살 통살 닭가슴살 허니소이",
            "kcal": 135,
            "protein": 21,
            "fat": 1.5,
            "carbs": 9,
            "number": 10,
            "gram": 100,
            "iscoupangfresh" : True,
            "category" : 1,
            "img" : "master_img/category/chicken-breast.jpg",
            "cookingoption" : 5,
            "link": "https://www.coupang.com/vp/products/6081081115?itemId=11273250763",
            "created_at": "2023-02-15",
            "updated_at": "2023-02-15"
        }
        return super().setUp()
    
    def test_food_add(self):
        response = self.client.post(self.url, self.food_data, format='json')
        self.assertEqual(response.status_code, 201)




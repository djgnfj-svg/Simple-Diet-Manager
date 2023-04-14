from rest_framework.test import APITestCase

#  make test DRF food add api
class FoodAddTest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Cooking-Category.json', '_Master_data/Foods.json']
    def setUp(self) -> None:
        self.url = '/api/meals/'
        return super().setUp()
    

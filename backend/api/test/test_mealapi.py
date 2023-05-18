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

from foods.models import FoodCategory
from meals.models import Meal


class MealAPITest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']

    def setUp(self):
        self.url = "/api/meals/"
        self.data = {
            "foods" : [1,2,3],
            "category" : 1
        }
        Meal.objects.meal_create(
            foods = [1,2,3],
            category=FoodCategory.objects.get(id=1)
        )
        pass
    
    def test_not_create_duplicated_foods(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(Meal.objects.count(), 1)

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.post(self.url, data=self.data)
        response = self.client.get(self.url + "1/")
        self.assertEqual(response.status_code, 200)
    
    def test_create(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        response = self.client.post(self.url, data=self.data)
        self.data["foods"] = [1,2,3,4]
        response = self.client.put(self.url + "1/", data=self.data)
        self.assertEqual(response.status_code, 200)
    
    def test_delete(self):
        response = self.client.post(self.url, data=self.data)
        response = self.client.delete(self.url + "1/")
        self.assertEqual(response.status_code, 204)

    def test_delete_fail(self):
        response = self.client.delete(self.url + "100/")
        self.assertEqual(response.status_code, 404)
    
    def test_create_fail(self):
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, 400)

    def test_update_fail(self):
        response = self.client.post(self.url, data=self.data)
        response = self.client.put(self.url + "1/", data={})
        self.assertEqual(response.status_code, 400)

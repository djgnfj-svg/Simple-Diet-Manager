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

class FoodAPITest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']
    
    def setUp(self):
        self.url = "/api/foods/"
        self.food_data = {
            "name": "한끼통살 통살 닭가슴살 허니소이2",
            "kcal": 135,
            "protein": 21,
            "fat": 15,
            "carbs": 9,
            "number": 10,
            "gram": 100,
            "category": 1,
            "link": "https://www.coupang.com/vp/products/6081081115?itemId=11273250763",
        }
        pass

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.url + "1/")
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(self.url, data=self.food_data)
        self.assertEqual(response.status_code, 201)
    
    def test_create_fail(self):
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, 400)
    
    def test_update(self):
        response = self.client.post(self.url, data=self.food_data)
        self.food_data["name"] = "한끼통살 통살 닭가슴살 허니소이3"
        response = self.client.put(self.url + "1/", data=self.food_data)
        self.assertEqual(response.status_code, 200)

    def test_update_fail(self):
        response = self.client.put(self.url + "1/", data={})
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        response = self.client.delete(self.url + "1/")
        self.assertEqual(response.status_code, 204)
    
    def test_delete_fail(self):
        response = self.client.delete(self.url + "999/")
        self.assertEqual(response.status_code, 404)
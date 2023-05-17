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

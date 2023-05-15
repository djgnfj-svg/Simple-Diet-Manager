# API테스트
'''
생성
삭제
수정
조회

실패
초과 미만 없음
'''

#drf TEST
# Path: api\test\test_dietapi.py
from rest_framework.test import APITestCase

class DietAPITest(APITestCase):
    fixtures = ['_Master_data/Food-Category.json', '_Master_data/Foods.json']
    
    # MEAL처럼 한번에 create되게 하는 로직 만들면서 작성 지금은 여기까지
    def setUp(self) -> None:
        self.url = "/api/diets/"
        self.data = {
            
        }
        return super().setUp()

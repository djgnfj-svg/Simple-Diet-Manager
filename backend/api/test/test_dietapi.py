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
    fixtures = ['_Master_data/Food-Category.json',
                '_Master_data/Cooking-Category.json', '_Master_data/Foods.json']
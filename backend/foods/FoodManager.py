import random
from django.db.models import Q
from Utils.common.ManagerBase import ManagerBase

from foods.models import Food


# TODO : 영양소 full로직을 밖으로 가져가는 것은 좋지 않다.
# 352 비율로 식단을 만들어버리자

class FoodManager(ManagerBase):
    def __init__(self):
        pass
    
    def get_data(self, nutrient, food_number):
        # TODO : 예외처리를 해야합니다.
        q = Q()
        len = Food.objects.count()
        # 랜덤 숫자만들기
        food_number = random.randrange(0, len)
            
        food = Food.objects.filter().order_by("-" + nutrient)[food_number]
        return food
    
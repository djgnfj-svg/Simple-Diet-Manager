import random
from django.db.models import Q
from Utils.common.ManagerBase import ManagerBase

from foods.models import Food

class FoodManager(ManagerBase):
    def __init__(self):
        self.protein_full = False
        self.fat_full = False
        self.carbs_full = False

    def get_data(self, nutrient, food_number):
        # TODO : 예외처리를 해야합니다.
        q = Q()
        len = Food.objects.count()
        # 랜덤 숫자만들기
        food_number = random.randrange(0, len)
            
        food = Food.objects.filter().order_by("-" + nutrient)[food_number]
        return food
    
import random
from django.db.models import Q
from Utils.common.ManagerBase import ManagerBase

from foods.models import Food


class FoodManager(ManagerBase):
    def __init__(self):
        pass
    
    # TODO : ver0.2 에서 식품의 옵션을 넣을 수 있다
    def get_data(self, nutrient, food_number):
        q = Q()

        food = Food.objects.filter(q).order_by("-" + nutrient)[food_number]
        return food
    
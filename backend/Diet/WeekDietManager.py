from Utils.common.ManagerBase import ManagerBase
from Utils.Metabolic.MetabolicManager import Metabolic_Manager
from diet.DietManager import DietManager


class WeekDietManager(ManagerBase):
    def __init__(self):
        self.data = {}
    def get_data(self, data):
        day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        self.data = {}
        #1. 기초대사량 계산하기
        metabolic_manager = Metabolic_Manager()
        metabolic_data = metabolic_manager.get_data(data)

        #2. 섭취 영양소 만들기
        meal_count = data['meal_count']
        diet_status = data['diet_status']
        # meal_option = data['meal_option']
        meal_option = 0

        # diet_status 0: 유지 1: 감량 2: 증량(미구현)
        min_range = 0.8 if diet_status == 1 else 0.9
        max_range = 0.9 if diet_status == 1 else 1.0

        for day in day_of_week:
            _Diet = DietManager()
            self.data[day] = _Diet.get_data(metabolic_data, meal_option, meal_count, min_range, max_range)

        return self.data
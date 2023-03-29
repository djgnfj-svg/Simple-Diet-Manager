
from Utils.common.AssginerBase import AssignerBase
from Utils.Metabolic.MetabolicManager import Metabolic_Manager
from meal.MealManager import Meal_Manager


class Diet_Assigner(AssignerBase):
    def __init__(self):
        super().__init__()

    def assign_data(self, data):
        #1. 기초대사량 계산하기
        self.data = None
        metabolic_manager = Metabolic_Manager(data)
        metabolic_data = metabolic_manager.get_data()

        #2. 섭취 영양소 만들기
        meal_count = data['meal_count']
        diet_status = data['diet_status']

        # diet_status 0: 유지 1: 감량 2: 증량(미구현)
        min_range = 0.8 if diet_status == 1 else 0.9
        max_range = 0.9 if diet_status == 1 else 1.0

        #3. 식단 만들기
        #3.1 식사 가져오기
        # meal_option = data['meal_option']
        meal_option = [1]

        mael_manager = Meal_Manager(metabolic_data, meal_option, meal_count, min_range, max_range)
        mael_manager.get_data()
        
        #4. 식단 검증하기

    
    def get_data(self):
        return self.data
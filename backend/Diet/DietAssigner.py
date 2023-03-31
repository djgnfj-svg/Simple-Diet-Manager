
from Utils.common.AssginerBase import AssignerBase
from Utils.Metabolic.MetabolicManager import Metabolic_Manager
from meal.MealManager import Meal_Manager


class Diet_Assigner(AssignerBase):
    def __init__(self):
        self.data = {}
        super().__init__()

    # 기초대사량 + 옵션 + 다이어트 유무 + 식단 개수 +min_range + max_range + 이미들어가있는 음식의 데이터
    def assign_data(self, metabolic_data, meal_option, meal_count, min_range, max_range):
        #3. 식단 만들기
        #3.1 식사 가져오기
        # meal_option = data['meal_option']
        if meal_count == 1:
            meals = ["breakfast"]
            meals_nutrient = [1]
        elif meal_count == 2:
            meals = ["breakfast", "lunch"]
            meals_nutrient = [0.6, 0.4]
        elif meal_count == 3:
            meals = ["breakfast", "lunch", "dinner"]
            meals_nutrient = [0.4, 0.3, 0.3]

        meal_manager = Meal_Manager()
        # 1.끼니별로 기초대사량 나누기
        # get_data에 끼니영양소 + 
        for meal, nutrient_range in zip(meals, meals_nutrient):
            need_nutrient = {}
            need_nutrient["kcal"] = metabolic_data["total_kcal"] * nutrient_range
            need_nutrient["protein"] = metabolic_data["total_protein"] * nutrient_range
            need_nutrient["fat"] = metabolic_data["total_fat"] * nutrient_range
            need_nutrient["carbs"] = metabolic_data["total_carbs"] * nutrient_range
            self.data[meal] = meal_manager.get_data(need_nutrient, meal_option, min_range, max_range)
            self.data[meal+"_need_nutrient"] = need_nutrient
        #4. 식단 검증하기
    def get_data(self):
        return self.data
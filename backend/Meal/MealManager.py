from Utils.common.ManagerBase import ManagerBase
from meal.MealAssigner import Meal_Assigner

class Meal_Manager(ManagerBase):
    def __init__(self, metabolic_data, meal_option, meal_count, min_range, max_range):
        # _meal = Meal_Assigner()
        # _meal.assign_data()
        # self.data = _meal.get_data()
        self.data = None

    def get_data(self):
        return self.data
from Utils.common.ManagerBase import ManagerBase
from Utils.Metabolic.MetabolicManager import MetabolicManager
from Utils.nutrient.Nutrient import NutrientCalculator as nutrientCal
from diets.models import Diet
from diets.DietManager import DietManager
from django.db.models import Q

class WeekDietManager(ManagerBase):
    def __init__(self):
        self.data = {}
        self.day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    def get_data(self, data):
        # diet_status 0: 유지 1: 감량 2: 증량(미구현)
        self.data["diet_status"] = data['diet_status']
        
        meal_count = data['meal_count']
        min_range = 0.8 if data['diet_status'] == 1 else 0.9
        max_range = 0.9 if data['diet_status'] == 1 else 1.0
        
        metabolic_manager = MetabolicManager()
        metabolic = metabolic_manager.get_data(data)
        self._metabolic_cal(metabolic, min_range, max_range)

        for day in self.day_of_week:
            q = Q()
            q &= Q(diet_kcal__gte=self.data["min_nutrient"]["kcal"], diet_kcal__lte=self.data["max_nutrient"]["kcal"])
            q &= Q(diet_protein__gte=self.data["min_nutrient"]["protein"], diet_protein__lte=self.data["max_nutrient"]["protein"])
            q &= Q(diet_fat__gte=self.data["min_nutrient"]["fat"], diet_fat__lte=self.data["max_nutrient"]["fat"])
            q &= Q(diet_carbs__gte=self.data["min_nutrient"]["carbs"], diet_carbs__lte=self.data["max_nutrient"]["carbs"])

            _Diet = DietManager(meal_count)

            self.data[day] = _Diet.get_data(metabolic, min_range, max_range)
            # Diet.objects.create(**self.data[day])

        return self.data
    
    def _metabolic_cal(self, metabolic_data, min_range, max_range):
        self.data["min_nutrient"] = {}
        self.data["min_nutrient"]["kcal"] = nutrientCal.cal_range(metabolic_data["metabolism_kcal"], min_range)
        self.data["min_nutrient"]["carbs"] = nutrientCal.cal_range(metabolic_data["metabolism_carbs"], min_range)
        self.data["min_nutrient"]["protein"] = nutrientCal.cal_range(metabolic_data["metabolism_protein"], min_range)
        self.data["min_nutrient"]["fat"] = nutrientCal.cal_range(metabolic_data["metabolism_fat"], min_range)

        self.data["max_nutrient"] = {}
        self.data["max_nutrient"]["kcal"] = nutrientCal.cal_range(metabolic_data["metabolism_kcal"], max_range)
        self.data["max_nutrient"]["carbs"] = nutrientCal.cal_range(metabolic_data["metabolism_carbs"], max_range)
        self.data["max_nutrient"]["protein"] = nutrientCal.cal_range(metabolic_data["metabolism_protein"], max_range)
        self.data["max_nutrient"]["fat"] = nutrientCal.cal_range(metabolic_data["metabolism_fat"], max_range)
        
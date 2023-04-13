from Utils.common.ManagerBase import ManagerBase
from Utils.Metabolic.MetabolicManager import MetabolicManager
from Utils.nutrient.Nutrient import NutrientCalculator as nc
from Utils.functions.nutrient_utils import init_nutrient
from accounts.models import UserBodyInfo
from diets.models import WeekDiet
from diets.DietManager import DietManager
from django.db.models import Q

class WeekDietManager(ManagerBase):
    def __init__(self):
        self.data = {}
        self.day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']

    # TODO : 일단 instance하고 data를 따로만들자
    def get_data(self, meal_count, userbody: UserBodyInfo, metabolic, min_range, max_range):
        week_min_nuturent, week_max_nutrient = self._cal_week_nutirient(metabolic, min_range, max_range)

        q = Q()
        q &= Q(week_kcal__gte=week_min_nuturent["kcal"], week_kcal__lte=week_max_nutrient["kcal"])
        q &= Q(week_protein__gte=week_min_nuturent["protein"], week_protein__lte=week_max_nutrient["protein"])
        q &= Q(week_fat__gte=week_min_nuturent["fat"], week_fat__lte=week_max_nutrient["fat"])
        q &= Q(week_carbs__gte=week_min_nuturent["carbs"], week_carbs__lte=week_max_nutrient["carbs"])
        
        week_diet = WeekDiet.objects.filter(q)

        if week_diet.count() > 0:
            return week_diet[0] # 0번쨰 인지는 아직 미정이다.
        else :
            # 주간 식단 생성
            diet_list = []
            week_data = {}
            init_nutrient(week_data)

            for day in self.day_of_week:
                diet_manger = DietManager(meal_count)
                
                _diet = diet_manger.get_data(metabolic, min_range, max_range)

                week_data["kcal"] += _diet.diet_kcal
                week_data["protein"] += _diet.diet_protein
                week_data["fat"] += _diet.diet_fat
                week_data["carbs"] += _diet.diet_carbs
                diet_list.append(_diet)
                

            week_diet = WeekDiet.objects.create(
                week_kcal=week_data["kcal"],
                week_protein=week_data["protein"],
                week_fat=week_data["fat"],
                week_carbs=week_data["carbs"],
                bodyinfo=userbody,
            )
            week_diet.diets.set(diet_list)

        return week_diet
    
    def _cal_week_nutirient(self, metabolic_data, min_range, max_range):
        min_week_nutrient = {}
        min_week_nutrient["kcal"] = nc.cal_range(metabolic_data["metabolism_kcal"], min_range) * 6
        min_week_nutrient["carbs"] = nc.cal_range(metabolic_data["metabolism_carbs"], min_range) * 6
        min_week_nutrient["protein"] = nc.cal_range(metabolic_data["metabolism_protein"], min_range) * 6
        min_week_nutrient["fat"] = nc.cal_range(metabolic_data["metabolism_fat"], min_range) * 6

        max_week_nutrient = {}
        max_week_nutrient["kcal"] = nc.cal_range(metabolic_data["metabolism_kcal"], max_range) * 6
        max_week_nutrient["carbs"] = nc.cal_range(metabolic_data["metabolism_carbs"], max_range) * 6
        max_week_nutrient["protein"] = nc.cal_range(metabolic_data["metabolism_protein"], max_range) * 6
        max_week_nutrient["fat"] = nc.cal_range(metabolic_data["metabolism_fat"], max_range) * 6

        return min_week_nutrient, max_week_nutrient


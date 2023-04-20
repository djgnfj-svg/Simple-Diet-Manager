from accounts.models import UserBodyInfo
from common.manager.base_manager import DietManagerBase
from common.manager.diet_manager import DietManager
from core.nutrient import NutrientCalculator as nc
from core.nutrient_utils import add_nutrient, init_nutrient
from diets.models import WeekDiet


class WeekDietManager(DietManagerBase):
    def __init__(self):
        pass

    def get_data(self, meal_count, userbody: UserBodyInfo, metabolic, min_range, max_range):
        min_nutrient, max_nutrient = self._cal_week_nutirient(metabolic, min_range, max_range)
        week_diet = self.find_instance(WeekDiet, "week_", min_nutrient, max_nutrient)

        # TODO : 0번째인지는 미정이다.
        if week_diet.count() > 0:
            return week_diet[0] 
        else :
            return self.make_instance(meal_count, metabolic, min_range, \
                                      max_range, userbody)
    
    def make_instance(self,meal_count, metabolic, min_range, max_range, userbody):
        week_data = {}
        diet_list = []
        init_nutrient(week_data)
        
        for i in range(0,3):
            diet_manger = DietManager(meal_count)
            _diet = diet_manger.get_data(metabolic, min_range, max_range, i)
            
            add_nutrient(week_data, _diet, nutrient_prefix="diet_")
            diet_list.append(_diet)

        n_diets = len(diet_list)
        for i in range(n_diets):
            diet = diet_list[i]
            add_nutrient(week_data, diet, nutrient_prefix="diet_")
            diet_list.append(diet)

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


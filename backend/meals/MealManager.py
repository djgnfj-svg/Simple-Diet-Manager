from django.db.models import Q

from foods.models import Food

from meals.models import Meal

from Utils.common.ManagerBase import ManagerBase
from Utils.functions.nutrient_utils import init_nutrient, add_nutrietn, make_nutrient

class MealChecker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check_all_nutrient(min, max, obj, prefix=None):
        if min["kcal"] <= obj[prefix+"kcal"] <= max["kcal"] and \
            min["protein"] <= obj[prefix+"protein"] <= max["protein"] and \
            min["fat"] <= obj[prefix+"fat"] <= max["fat"] and \
            min["carbs"] <= obj[prefix+"carbs"] <= max["carbs"]:
            return True
        else:
            return False
    
    @staticmethod
    def check_nutirent(min_nutrient, max_nutrient, nutrient, nutrient_name, prefix=None):
        if min_nutrient[nutrient_name] <= nutrient[prefix + nutrient_name]:
            return True
        else:
            return False

    @staticmethod
    def check_food_over_nutrient(nutrient, max_nutrient, nutrient_name, food:Food, prefix=None):
        if nutrient[prefix + nutrient_name] + getattr(food, nutrient_name) > max_nutrient[nutrient_name]:
            return True
        else:
            return False
        
# TODO : 이딴게 코드니... 조져야한다.
class MealMakeManager():
    def __init__(self):
        self.data = {}
        self.protein_full = False
        self.fat_full = False
        self.carbs_full = False

    def meke_meal_range(self,start, stop, step,food:Food = None):
        for kcal in range(start, stop, step):
            min, max = make_nutrient(kcal)
            self.make_meal(min, max, food)


    def make_meal(self, min_nutrient, max_nutrient, _food:Food=None):
        current_nutrient = {}

        food_list = []
        init_nutrient(current_nutrient, prefix="current_")

        if _food:
            food_list.append(_food)
            add_nutrietn(current_nutrient, _food, prefix="current_")

        nutrient = ["kcal", "protein", "fat", "carbs"]

        # TODO : 일단 임시 방편...
        min_nutrient["protein"] *= 0.5
        min_nutrient["fat"] *= 0.5
        min_nutrient["carbs"] *= 0.5

        food_focus = 0
        nutrient_focus = 1
        while nutrient_focus < 4:
            # 현재 영양소를 만족했는가?
            if  MealChecker.check_nutirent(min_nutrient, max_nutrient, current_nutrient, nutrient[nutrient_focus], prefix="current_"):
                nutrient_focus += 1
                food_focus = 0
                continue

            # 현재 영양소가 가장 큰 음식을 가져온다.
            food = Food.objects.order_by("-" + nutrient[nutrient_focus])[food_focus]

            # 그것을 추가할때 너무 오버된다면 다음 으로 넘아간다.
            if MealChecker.check_food_over_nutrient(current_nutrient, max_nutrient, nutrient[nutrient_focus], food, prefix="current_"):
                food_focus += 1
                continue

            add_nutrietn(current_nutrient, food, prefix="current_")
            food_list.append(food)
            food_focus += 1
                
        meal = Meal.objects.create(
            meal_kcal= current_nutrient["current_kcal"],
            meal_protein= current_nutrient["current_protein"],
            meal_fat= current_nutrient["current_fat"],
            meal_carbs= current_nutrient["current_carbs"],
        )
        foods = Food.objects.filter(id__in=[food.id for food in food_list])
        meal.foods.set(foods)
        meal.save()
        return meal
    
class MealManager(ManagerBase):
    def __init__(self):
        self.data = {}

    # TODO : 요일 받기 6/3 해가 지고 남머지로 식단 추출하면됨 어짜피 삼시새끼로 할꺼니까
    def get_data(self, need_nutrient, min_range, max_range):
        min_range -= 0.1
        min_nutrient, max_nutrient = make_nutrient(need_nutrient["need_kcal"])
        q = Q()

        q &= Q(meal_protein__gte=min_nutrient["kcal"], meal_protein__lte=max_nutrient["kcal"])
        q &= Q(meal_fat__gte=min_nutrient["fat"], meal_fat__lte=max_nutrient["fat"])
        q &= Q(meal_carbs__gte=min_nutrient["carbs"], meal_carbs__lte=max_nutrient["carbs"])
        q &= Q(meal_kcal__gte=min_nutrient["kcal"], meal_kcal__lte=max_nutrient["kcal"])

        meal = Meal.objects.filter(q)
        
        if meal.count() > 2:
            return meal[0]
        else :
            makemanager = MealMakeManager()
            meal = makemanager.make_meal(min_nutrient, max_nutrient)
            return meal

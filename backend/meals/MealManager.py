from django.db.models import Q

from foods.models import Food
from foods.FoodManager import FoodManager

from meals.models import Meal

from Utils.common.ManagerBase import ManagerBase
from Utils.functions.nutrient_utils import init_nutrient, add_nutrietn

class MealMakeManager(ManagerBase):
    def __init__(self):
        self.data = {}
        self.protein_full = False
        self.fat_full = False
        self.carbs_full = False

    def check_nutrient(self, min_nutrient, max_nutrient, current_nutrient):
        if min_nutrient["kcal"] <= current_nutrient["current_kcal"] <= max_nutrient["kcal"] and \
            min_nutrient["protein"] <= current_nutrient["current_protein"] <= max_nutrient["protein"] and \
            min_nutrient["fat"] <= current_nutrient["current_fat"] <= max_nutrient["fat"] and \
            min_nutrient["carbs"] <= current_nutrient["current_carbs"] <= max_nutrient["carbs"]:
            return True
        else:
            return False
    def check_add_nutrient(self, current_nutrient, food, min_nutrient, max_nutrient, nutrient):
        if current_nutrient["current_" + nutrient] + getattr(food, nutrient) <= max_nutrient[nutrient]:
            return True
        else:
            return False
    
    def check_current_nutrient(self, current_nutrient, min_nutrient, max_nutrient, nutrient):
        if max_nutrient[nutrient] <= current_nutrient["current_" + nutrient]:
            return True
        else:
            return False
    
    def tempcheck(self, current_nutrient, min_nutrient, nutrient):
        if min_nutrient[nutrient] <= current_nutrient["current_" + nutrient]:
            return True
        else:
            return False

    def make_meal(self, min_nutrient, max_nutrient, food:Food):
        # 식단에 음식을 추사할 함수
        current_nutrient = {}
        init_nutrient(current_nutrient, prefix="current_")
        food_list = []
        food_list.append(food)

        # 음식을 가져와 현재영양소에 추가한다
        # 현재영양소가 최소 또는 최대 영양소를 벗어나면
        # 음식을 제거하고 다시 반복한다.
        # 최소영양소와 최대영양소를 벗어나지 않으면
        # 음식을 현재영양소에 추가하고 음식리스트에 append하는 로직

        nutrient = ["kcal", "protein", "fat", "carbs"]
        for i in nutrient:
            current_nutrient["current_" + i] += getattr(food, i)
        nutrient_focus = 1
        food_focus = 0
        # while not self.check_nutrient(min_nutrient, max_nutrient, current_nutrient):
        while nutrient_focus < 4:
            _food = Food.objects.order_by("-" + nutrient[nutrient_focus])[food_focus]
            # 이미 초과했다면 그 영양소는 넘어가라
            if self.check_current_nutrient(current_nutrient, min_nutrient, max_nutrient, nutrient[nutrient_focus]):
                nutrient_focus += 1
                food_focus = 0
                continue
            if self.check_add_nutrient(current_nutrient, _food, min_nutrient, max_nutrient, nutrient[nutrient_focus]):
                food_list.append(_food)
                for i in nutrient:
                    current_nutrient["current_" + i] += getattr(_food, i)
                if self.tempcheck(current_nutrient, min_nutrient, nutrient[nutrient_focus]):
                    nutrient_focus += 1
                    food_focus = 0
                else:
                    food_focus += 1
            else :
                food_focus += 1

        print(food_list)
        # meal.save()



    def get_data(self, need_nutrient, meal_option, min_range, max_range):
        min_range -= 0.5
        food_manager = FoodManager()

        meal_data = {}
        init_nutrient(meal_data, prefix="meal_")
        meal_data["foods"] = {}
        
        food_list = []
        food_number = 0

        nutrient_number = 0
        nutrient_list = ["protein", "fat", "carbs"]

        while not self.carbs_full:
            meal_data["foods"][food_number] = {}
            food = food_manager.get_data(nutrient_list[nutrient_number], food_number)
            add_nutrietn(meal_data, food, prefix="meal_")

            food_list.append(food)
            meal_data["foods"][food_number]["food_name"] = food.name

            # TODO : 우아하게...
            if meal_data["meal_protein"] > need_nutrient["need_protein"] * min_range and \
                not self.protein_full:
                self.protein_full = True
                nutrient_number = 1
                food_number = 0

            if meal_data["meal_fat"] > need_nutrient["need_fat"] * min_range and \
                not self.fat_full and self.protein_full:
                self.fat_full = True
                nutrient_number = 2
                food_number = 0
            
            if meal_data["meal_carbs"] > need_nutrient["need_carbs"] * min_range and \
                self.fat_full and self.protein_full :
                self.carbs_full = True
                break
            food_number += 1

        meal = Meal(
            meal_kcal= meal_data["meal_kcal"],
            meal_protein= meal_data["meal_protein"],
            meal_fat= meal_data["meal_fat"],
            meal_carbs= meal_data["meal_carbs"],
        )
        foods = Food.objects.filter(id__in=[food.id for food in food_list])
        meal.save(foods=foods)
        meal_data["meal_name"] = meal.name
        return meal_data
    
class MealManager(ManagerBase):
    def __init__(self):
        self.data = {}

    def get_data(self, need_nutrient, meal_option, min_range, max_range):
        # min_range -= 0.2
        q = Q()

        q &= Q(meal_protein__gte=need_nutrient["need_protein"]*min_range, meal_protein__lte=need_nutrient["need_protein"]*max_range)
        q &= Q(meal_fat__gte=need_nutrient["need_fat"]*min_range, meal_fat__lte=need_nutrient["need_fat"]*max_range)
        q &= Q(meal_carbs__gte=need_nutrient["need_carbs"]*min_range, meal_carbs__lte=need_nutrient["need_carbs"]*max_range)
        q &= Q(meal_kcal__gte=need_nutrient["need_kcal"]*min_range, meal_kcal__lte=need_nutrient["need_kcal"]*max_range)

        meal = Meal.objects.filter(q)
        if meal:
            # serializer 만들어서 리턴하기
            # ver01에는 랜덤을 사용하고 추후 수저
            return meal[0]
        else :
            makemanager = MealMakeManager()
            meal = makemanager.get_data(need_nutrient, meal_option, min_range, max_range)
            return meal

from Utils.common.ManagerBase import ManagerBase
from food.models import Food
from meal.models import Meal
from food.FoodManager import FoodManager
from django.db.models import Q

class Meal_Manager(ManagerBase):
    def __init__(self):
        self.data = None

    def get_data(self, meal_nutrient, meal_option, min_range, max_range):
        # min_range -= 0.2
        q = Q()

        q &= Q(meal_protein__gte=meal_nutrient["protein"]*min_range, meal_protein__lte=meal_nutrient["protein"]*max_range)
        q &= Q(meal_fat__gte=meal_nutrient["fat"]*min_range, meal_fat__lte=meal_nutrient["fat"]*max_range)
        q &= Q(meal_carbs__gte=meal_nutrient["carbs"]*min_range, meal_carbs__lte=meal_nutrient["carbs"]*max_range)
        q &= Q(meal_kcal__gte=meal_nutrient["kcal"]*min_range, meal_kcal__lte=meal_nutrient["kcal"]*max_range)

        meal = Meal.objects.filter(q)
        if meal:
            # serializer 만들어서 리턴하기
            
            meal_data = {}
            meal_data["meal_kcal"] = 0
            meal_data["meal_protein"] = 0
            meal_data["meal_fat"] = 0
            meal_data["meal_carbs"] = 0
            meal_data["foods"] = {}
            print("설마 여기로 들어오니?")
            return meal[0]
        else :
            meal = self.make_meal(meal_nutrient, meal_option, min_range, max_range)
            return meal

    def make_meal(self, meal_nutrient, meal_option, min_range, max_range):
        # TODO : 우아하게 바꾸기
        min_range -= 0.5
        food_manager = FoodManager()
        meal_data = {}
        meal_data["meal_kcal"] = 0
        meal_data["meal_protein"] = 0
        meal_data["meal_fat"] = 0
        meal_data["meal_carbs"] = 0
        meal_data["foods"] = {}
        food_list = []

        food_number = 0
        nutrient_number = 0
        nutrient_list = ["protein", "fat", "carbs"]
        while not food_manager.carbs_full:
            meal_data["foods"][food_number] = {}
            food = food_manager.get_data(nutrient_list[nutrient_number], food_number)
            if food is None:
                raise Exception("음식이 없습니다.")
            meal_data["meal_kcal"] += food.kcal
            meal_data["meal_protein"] += food.protein
            meal_data["meal_fat"] += food.fat
            meal_data["meal_carbs"] += food.carbs

            food_list.append(food)
            meal_data["foods"][food_number]["food_name"] = food.name

            # TODO : 우아하게...
            if meal_data["meal_protein"] > meal_nutrient["protein"] * min_range and \
                not food_manager.protein_full:
                setattr(food_manager, "protein_full",True)
                nutrient_number = 1
                food_number = 0

            if meal_data["meal_fat"] > meal_nutrient["fat"] * min_range and \
                not food_manager.fat_full and food_manager.protein_full:
                setattr(food_manager, "fat_full",True)
                nutrient_number = 2
                food_number = 0
            
            if meal_data["meal_carbs"] > meal_nutrient["carbs"] * min_range and \
                food_manager.fat_full and food_manager.protein_full :
                setattr(food_manager, "carbs_full",True)
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
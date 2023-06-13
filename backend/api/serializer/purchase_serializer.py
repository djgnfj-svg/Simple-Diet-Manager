from rest_framework import serializers

from diets.models import Diet
from meals.models import Meal

# TODO : 리팩토링 필요

class MealPurchaseSerializer(serializers.Serializer):
    Food_Purchase_info = serializers.SerializerMethodField()

    class Meta:
        fields = ("Food_Purchase_info")

    def get_Food_Purchase_info(self, obj:Meal) -> list:
        rtn = []
        for _, food in enumerate(obj.foods.all()):
            temp = {}
            temp["food_name"] = food.name
            temp["food_link"] = food.link
            rtn.append(temp)
        return rtn

class DietPurchaseSerializer(serializers.Serializer):
    Meal_Purchase_info = serializers.SerializerMethodField()

    class Meta:
        fields = ("Meal_Purchase_info")

    def get_Meal_Purchase_info(self, obj : Diet) -> list:
        rtn = []
        if obj.meals.count() == 1:
            obj_list = []
            for _ in range(obj.meal_count):
                obj_list.append(obj.meals.first())
        else:
            obj_list = obj.meals.all()


        for i, meal in enumerate(obj_list):
            foods = MealPurchaseSerializer(meal).data

            if i == 0:
                for food in foods["Food_Purchase_info"]:
                    temp = {}
                    temp["food_name"] = food["food_name"]
                    temp["food_link"] = food["food_link"]
                    temp["food_count"] = 1
                    rtn.append(temp)
                continue
            else :
                for food in foods["Food_Purchase_info"]:
                    for rtn_food in rtn:
                        if rtn_food["food_name"] == food["food_name"]:
                            rtn_food["food_count"] += 1
                            break
                    else:
                        temp = {}
                        temp["food_name"] = food["food_name"]
                        temp["food_link"] = food["food_link"]
                        temp["food_count"] = 1
                        rtn.append(temp)
        return rtn


class WeekDietPurchaseSerializer(serializers.Serializer):
    Diet_Purchase_info = serializers.SerializerMethodField()

    class Meta:
        fields = ("Diet_Purchase_info")

    def get_Diet_Purchase_info(self, obj) -> list:
        rtn = []

        for i, diet in enumerate(obj.diets.all()):
            meals = DietPurchaseSerializer(diet).data
            if i == 0:
                for meal in meals["Meal_Purchase_info"]:
                    temp = {}
                    temp["food_name"] = meal["food_name"]
                    temp["food_link"] = meal["food_link"]
                    temp["food_count"] = meal["food_count"]
                    rtn.append(temp)
                continue
            else :
                for meal in meals["Meal_Purchase_info"]:
                    for rtn_food in rtn:
                        if rtn_food["food_name"] == meal["food_name"]:
                            rtn_food["food_count"] += meal["food_count"]
                            break
                    else:
                        temp = {}
                        temp["food_name"] = meal["food_name"]
                        temp["food_link"] = meal["food_link"]
                        temp["food_count"] = meal["food_count"]
                        rtn.append(temp)
        # 구매해야하는 총량        
        for food in rtn:
            food["food_count"] *= 2

        # TODO 구매해야하는 제품의 갯수와 지켰을 경우 남는양
        # count로 나눠서 남은양 하고 몇개인지 거시기!
        return rtn
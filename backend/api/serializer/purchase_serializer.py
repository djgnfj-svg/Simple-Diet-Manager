from rest_framework import serializers


class MealPurchaseSerializer(serializers.Serializer):
    Food_Purchase_info = serializers.SerializerMethodField()

    class Meta:
        fields = ("Food_Purchase_info")

    def get_Food_Purchase_info(self, obj) -> list:
        rtn = {}
        for i, food in enumerate(obj.foods.all()):
            rtn[i] = f"{food.name} | {food.link}"
        return rtn

class DietPurchaseSerializer(serializers.Serializer):
    Meal_Purchase_info = serializers.SerializerMethodField()

    class Meta:
        fields = ("Meal_Purchase_info")

    def get_Meal_Purchase_info(self, obj) -> list:
        food_list = []
        rtn_list = []
        for meal in obj.meals.all():
            meal_food_info = MealPurchaseSerializer(meal).data
            for j in range(len(meal_food_info["Food_Purchase_info"])):
                food_name = meal_food_info["Food_Purchase_info"][j].split(" | ")[0]
                food_link = meal_food_info["Food_Purchase_info"][j].split(" | ")[1]
                if food_name not in food_list:
                    food_list.append(food_name)
                    rtn_list.append(f"{food_name} | {food_link} | {1}")
                else :
                    for k in range(len(rtn_list)):
                        if food_name in rtn_list[k]:
                            rtn_list[k] = f"{food_name} | {food_link} | {int(rtn_list[k].split(' | ')[-1]) + 1}"
        return rtn_list

class WeekDietPurchaseSerializer(serializers.Serializer):
    Diet_Purchase_info = serializers.SerializerMethodField()

    class Meta:
        fields = ("Diet_Purchase_info")

    # TODO : 결제페이지 지금 manytomany가 하나있을때 제대로 계산되지 않는 버그 있음
    def get_Diet_Purchase_info(self, obj) -> list:
        food_list = []
        rtn_list = []
        for i, diet in enumerate(obj.diets.all()):
            diet_food_info = DietPurchaseSerializer(diet).data
            for j in range(len(diet_food_info["Meal_Purchase_info"])):
                food_name = diet_food_info["Meal_Purchase_info"][j].split(" | ")[0]
                food_link = diet_food_info["Meal_Purchase_info"][j].split(" | ")[1]
                food_count = diet_food_info["Meal_Purchase_info"][j].split(" | ")[2]
                if food_name not in food_list:
                    food_list.append(food_name)
                    rtn_list.append(f"{food_name} | {food_link} | {food_count}")
                else :
                    for k in range(len(rtn_list)):
                        if food_name in rtn_list[k]:
                            rtn_list[k] = f"{food_name} | {food_link} | {int(rtn_list[k].split(' | ')[-1]) + int(food_count)}"
        rtn = {}
        for i, food in enumerate(rtn_list):
            temp = {}
            temp["name"] = food.split(" | ")[0]
            temp["link"] = food.split(" | ")[1]
            temp["count"] = food.split(" | ")[2]
            rtn[i] = temp
        return rtn
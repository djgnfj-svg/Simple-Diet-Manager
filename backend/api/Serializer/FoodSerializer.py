from rest_framework import serializers
from Utils.functions.nutrient_utils import make_nutrient
from meals.MealManager import MealMakeManager

from foods.models import CookingOption, Food, FoodCategory

#TODO : 관리자 권한 추가
class CookingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingOption
        fields = "__all__"

#TODO : 관리자 권한 추가
class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = "__all__"

#TODO : 관리자 권한 추가
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = ("created_at", "updated_at", "img")            

    def create(self, validated_data):        
        return super().create(validated_data)
from rest_framework import serializers
from Utils.functions.nutrient_utils import make_nutrient
from meals.MealManager import MealMakeManager

from foods.models import CookingOption, Food, FoodCategory

class CookingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingOption
        fields = "__all__"

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = "__all__"

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = ("created_at", "updated_at")            

    def create(self, validated_data):
        return super().create(validated_data)
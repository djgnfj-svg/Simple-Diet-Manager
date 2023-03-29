from rest_framework import serializers
from food.models import Food

from meal.models import Meal

#TODO : 관리자 권한 추가
class MealFoodSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("id", "name")


class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerialzier(many=True)
    meal_video = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    class Meta:
        model = Meal
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
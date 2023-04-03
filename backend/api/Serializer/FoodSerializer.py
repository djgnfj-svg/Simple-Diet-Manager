from rest_framework import serializers

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
        fields = "__all__"
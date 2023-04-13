from rest_framework import serializers

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
        fields = ("id",)
        # exclude = ("created_at", "updated_at")            

    
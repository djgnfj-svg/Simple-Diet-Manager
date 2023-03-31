from rest_framework import serializers

from meal.models import Meal


class MealSerializer(serializers.ModelSerializer):
    meal_kcal = serializers.IntegerField(read_only=True, default=0)
    meal_protein = serializers.IntegerField(read_only=True, default=0)
    meal_fat = serializers.IntegerField(read_only=True, default=0)
    meal_carbs = serializers.IntegerField(read_only=True, default=0)
    meal_video = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    class Meta:
        model = Meal
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)
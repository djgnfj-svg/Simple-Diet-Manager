from rest_framework import serializers

from api.serializer.food_serializer import FoodSerializer

from foods.models import Food
from meals.models import Meal


class MealSerializer(serializers.ModelSerializer):
    foods = serializers.PrimaryKeyRelatedField(many=True, queryset=Food.objects.all())
    
    kcal = serializers.IntegerField(read_only=True, default=0)
    protein = serializers.IntegerField(read_only=True, default=0)
    fat = serializers.IntegerField(read_only=True, default=0)
    carbs = serializers.IntegerField(read_only=True, default=0)
    
    class Meta:
        model = Meal
        exclude = ('created_at', 'updated_at')
        
    def to_representation(self, instance):
        rtn = super().to_representation(instance)
        rtn['foods'] = FoodSerializer(instance.foods.all(), many=True).data
        return rtn
    
    def validate(self, data):
        if 'foods' not in data:
            raise serializers.ValidationError("foods field is required")
        return data
    
    def create(self, validated_data):
        instance = Meal.objects.meal_create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        try:
            instance = Meal.objects.meal_update(**validated_data)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return instance
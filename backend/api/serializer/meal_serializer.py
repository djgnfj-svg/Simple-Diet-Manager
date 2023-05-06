from rest_framework import serializers

from api.serializer.food_serializer import FoodSerializer
from foods.models import Food, FoodCategory
from meals.models import Meal


class MealSerializer(serializers.ModelSerializer):
    foods = serializers.PrimaryKeyRelatedField(many=True, queryset=Food.objects.all())
    
    meal_kcal = serializers.IntegerField(read_only=True, default=0)
    meal_protein = serializers.IntegerField(read_only=True, default=0)
    meal_fat = serializers.IntegerField(read_only=True, default=0)
    meal_carbs = serializers.IntegerField(read_only=True, default=0)
    
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
    
    # 이부분 수정하면 됨
    def create(self, validated_data):
        # 여기서 meal_create인가로 받으면 국받일듯
        instance = super().create(validated_data)
        if instance.foods.count() < 1:
            raise serializers.ValidationError('음식이 없습니다.')
        if instance.foods.count() != 1 and instance.name == '':
            for i, food in enumerate(instance.foods.all()):
                name.join(', ', FoodCategory.objects.get(id = instance.foods.all()[i].category_id).name)
                instance.meal_kcal += food.kcal
                instance.meal_protein += food.protein
                instance.meal_fat += food.fat
                instance.meal_carbs += food.carbs
        else:
            name = FoodCategory.objects.get(id = instance.foods.all()[0].category_id).name
            instance.meal_kcal = instance.foods.all()[0].kcal
            instance.meal_protein = instance.foods.all()[0].protein
            instance.meal_fat = instance.foods.all()[0].fat
            instance.meal_carbs = instance.foods.all()[0].carbs
        instance.name = name
        instance.meal_img = instance.foods.order_by('-protein')[0].img
        instance.save()
        return instance

    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.meal_kcal = 0
        instance.meal_protein = 0
        instance.meal_fat = 0
        instance.meal_carbs = 0
        
        name = ''
        for i, food in enumerate(instance.foods.all()):
            name.join(', ', FoodCategory.objects.get(id = instance.foods.all()[i].category_id).name)
            instance.meal_kcal += food.kcal
            instance.meal_protein += food.protein
            instance.meal_fat += food.fat
            instance.meal_carbs += food.carbs

        instance.name = name
        instance.meal_img = instance.foods.order_by('-protein')[0].img
        instance.save()
        return instance
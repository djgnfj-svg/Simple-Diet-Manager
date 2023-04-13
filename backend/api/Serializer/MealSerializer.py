from rest_framework import serializers

from api.Serializer.FoodSerializer import FoodSerializer

from foods.models import FoodCategory

from meals.models import Meal


class MealSerializer(serializers.ModelSerializer):
    meal_kcal = serializers.IntegerField(read_only=True, default=0)
    meal_protein = serializers.IntegerField(read_only=True, default=0)
    meal_fat = serializers.IntegerField(read_only=True, default=0)
    meal_carbs = serializers.IntegerField(read_only=True, default=0)
    class Meta:
        model = Meal
        exclude = ('created_at', 'updated_at', 'foods')


    def create(self, validated_data):
        instance = super().create(validated_data)
        
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
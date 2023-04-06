from rest_framework import serializers

from meals.models import Meal

class MealViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"

class MealSerializer(serializers.ModelSerializer):
    meal_kcal = serializers.IntegerField(read_only=True, default=0)
    meal_protein = serializers.IntegerField(read_only=True, default=0)
    meal_fat = serializers.IntegerField(read_only=True, default=0)
    meal_carbs = serializers.IntegerField(read_only=True, default=0)
    meal_video = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    class Meta:
        model = Meal
        fields = "__all__"

    # admin을 사용할꺼면 이로직을 그대로 사용해야한다.
    def create(self, validated_data):
        instance = super().create(validated_data)
        if validated_data.get('meal_img') is None:
            instance.meal_img = instance.foods.order_by('-protein')[0].img
        if instance.name == '':
            # TODO : 카테고리로 이름을 정해도 된다.
            if len(instance.foods.order_by('-protein')[0].name) < 5:
                name = instance.foods.order_by('-protein')[0].name
            else :
                name = instance.foods.order_by('-protein')[0].name[:5]
            instance.name = f"{name} 외 {instance.foods.count() - 1}개"

        for food in instance.foods.all():
            instance.meal_kcal += food.kcal
            instance.meal_protein += food.protein
            instance.meal_fat += food.fat
            instance.meal_carbs += food.carbs

        if not instance.meal_img:
            print(instance.foods.order_by('-protein')[0].img)
            instance.meal_img = instance.foods.order_by('-protein')[0].img
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.meal_kcal = 0
        instance.meal_protein = 0
        instance.meal_fat = 0
        instance.meal_carbs = 0
        if len(instance.foods.order_by('-protein')[0].name) < 5:
            name = instance.foods.order_by('-protein')[0].name
        else :
            name = instance.foods.order_by('-protein')[0].name[:5]
        instance.name = f"{name} 외 {instance.foods.count() - 1}개"

        for food in instance.foods.all():
            instance.meal_kcal += food.kcal
            instance.meal_protein += food.protein
            instance.meal_fat += food.fat
            instance.meal_carbs += food.carbs
        instance.save()

        return instance
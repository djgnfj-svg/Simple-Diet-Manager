from rest_framework import serializers
from accounts.models import UserBodyInfo
from api.Serializer.MealSerializer import MealSerializer
from Utils.Metabolic.MetabolicManager import MetabolicManager
from diets.DietManager import DietManager
from diets.models import Diet
from diets.WeekDietManager import WeekDietManager


class DietSerializer(serializers.ModelSerializer):
    meals = serializers.SerializerMethodField()

    diet_kcal = serializers.IntegerField(read_only=True, default=0)
    diet_protein = serializers.IntegerField(read_only=True, default=0)
    diet_fat = serializers.IntegerField(read_only=True, default=0)
    diet_carbs = serializers.IntegerField(read_only=True, default=0)
    
    class Meta:
        model = Diet
        fields = ("id","meals", "diet_kcal", "diet_protein", "diet_fat", "diet_carbs")
    def get_meals(self, obj) -> list:
        meals = {}
        meals_name_list = ['breakfast', 'lunch', 'dinner']

        for meal, meal_name in zip(obj.meals.all(), meals_name_list):
            meals[meal_name] = MealSerializer(meal).data
        return meals

class WeekDietSerializer(serializers.Serializer):
    diets = serializers.SerializerMethodField()

    class Meta:
        fields = ("diets", "diet_status")

    def get_diets(self, obj) -> list:
        diets = {}
        day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
        for diet, day in zip(obj.diets.all(), day_of_week):
            diets[day] = DietSerializer(diet).data
        
        return diets

class DietMakeSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('W', 'W'),
    )
    # BodyInfo
    age = serializers.IntegerField(min_value=20, max_value=100)
    weight = serializers.FloatField(min_value=50, max_value=150)
    height = serializers.FloatField(min_value=145, max_value=230)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    general_activity = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)

    # DietInfo
    meal_count = serializers.IntegerField(min_value=1, max_value=3)
    diet_status = serializers.IntegerField(min_value=0, max_value=2)

    
    def create(self, validated_data):
        # Body info 저장
        userbodyinfo = UserBodyInfo.objects.create(
            age=validated_data['age'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            gender = validated_data['gender'],
            general = validated_data['general_activity'],
            activity = validated_data['excise_activity'],
        )

        metabolic_manager = MetabolicManager()
        metabolic = metabolic_manager.get_data(validated_data)

        weekdietmanager = WeekDietManager()
        # diet_status 0: 유지 1: 감량 2: 증량(미구현)
        min_range = 0.8 if validated_data['diet_status'] == 1 else 0.9
        max_range = 0.9 if validated_data['diet_status'] == 1 else 1.0
        week_diet = weekdietmanager.get_data(validated_data["meal_count"], userbodyinfo, metabolic, min_range, max_range)

        rtn = WeekDietSerializer(week_diet).data
        
        rtn["diet_status"] = validated_data["diet_status"]
        rtn["min_nutrient"], rtn["max_nutrient"] = DietManager._cal_nutirient(metabolic, min_range, max_range)
        return rtn
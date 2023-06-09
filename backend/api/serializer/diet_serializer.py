from rest_framework import serializers

from api.serializer.meal_serializer import MealSerializer
from api.Utils.metabolic_utils import make_min_max_nutrient
from api.Utils.user_body_utils import save_userbody
from api.Utils.week_diet_utils import make_week_diet

from diets.models import Diet, WeekDiet
from foods.models import FoodCategory
from meals.models import Meal



class DietSerializer(serializers.ModelSerializer):
    meals = serializers.PrimaryKeyRelatedField(many=True, queryset=Meal.objects.all())

    kcal = serializers.IntegerField(read_only=True, default=0)
    protein = serializers.IntegerField(read_only=True, default=0)
    fat = serializers.IntegerField(read_only=True, default=0)
    carbs = serializers.IntegerField(read_only=True, default=0)
    meal_count = serializers.IntegerField(read_only=True, default=3)

    class Meta:
        model = Diet
        fields = ("id", "meals", "kcal",
                  "protein", "fat", "carbs", "meal_count")

    def get_meals(self, obj) -> list:
        meals = {}
        meals_name_list = ['breakfast', 'lunch', 'dinner'] if obj.meal_count == 3 else ['breakfast', 'lunch']
        if obj.meals.count() == 1:
            for i in meals_name_list:
                meals[i] = MealSerializer(obj.meals.first()).data
        else:
            for meal, meal_name in zip(obj.meals.all(), meals_name_list):
                meals[meal_name] = MealSerializer(meal).data
        return meals
    
    def to_representation(self, instance):
        rtn = super().to_representation(instance)
        rtn["meals"] = self.get_meals(instance)
        return rtn

class WeekDietSerializer(serializers.ModelSerializer):
    diets = serializers.SerializerMethodField()

    class Meta:
        model = WeekDiet
        fields = ("id", "diets")

    def get_diets(self, obj) -> list:
        diets = {}
        day_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
        for i, diet in enumerate(obj.diets.all()):
            diets[day_of_week[i]] = DietSerializer(diet).data
            diets[day_of_week[i+3]] = DietSerializer(diet).data
        return diets
    
class WeekDietMakeSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('W', 'W'),
    )
    age = serializers.IntegerField(min_value=20, max_value=100)
    height = serializers.IntegerField(min_value=145, max_value=230)
    weight = serializers.IntegerField(min_value=50, max_value=150)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    general_activity = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)
    
    meal_count = serializers.IntegerField(min_value=1, max_value=3)
    diet_status = serializers.IntegerField(min_value=0, max_value=2)
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=FoodCategory.objects.all())

    def create(self, validated_data, user=None):
        min_nutrient, max_nutrient = make_min_max_nutrient(validated_data)
        week_diet = make_week_diet(validated_data, min_nutrient, max_nutrient)
        
        if user is not None:
            save_userbody(user, validated_data, week_diet)

        rtn = WeekDietSerializer(week_diet).data
        rtn["diet_status"] = validated_data["diet_status"]
        rtn["min_nutrient"] = min_nutrient
        rtn["max_nutrient"] = max_nutrient
        return rtn

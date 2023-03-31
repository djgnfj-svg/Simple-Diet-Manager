from rest_framework import serializers
from diet.models import Diet

from diet.WeekDietManager import WeekDietManager

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'


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
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)

    # DietInfo
    iscoupangfresh = serializers.BooleanField(default=False)
    meal_count = serializers.IntegerField(min_value=1, max_value=3)
    diet_status = serializers.IntegerField(min_value=0, max_value=2)

    
    def create(self, validated_data):
        dietmanager = WeekDietManager()
        temp = dietmanager.get_data(validated_data)
        return temp
     
from rest_framework import serializers

from diet.DietManager import Diet_Manager


class DietMakeSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('W', 'W'),
    )
    age = serializers.IntegerField(min_value=20, max_value=100)
    weight = serializers.FloatField(min_value=40, max_value=150)
    height = serializers.FloatField(min_value=140, max_value=250)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)

    meal_count = serializers.IntegerField(min_value=1, max_value=3)
    
    def create(self, validated_data):
        print(validated_data)
        dietmanager = Diet_Manager()
        dietmanager.assign_data(validated_data)
        dietmanager.get_data()
        return validated_data
    
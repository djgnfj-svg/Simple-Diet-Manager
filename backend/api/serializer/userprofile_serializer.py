from rest_framework import serializers

from accounts.models import BodyInfoRecord



# 몸무게와 그의 식단들의 id를 리턴해야한다.
class UserProfileSerializer(serializers.Serializer):
    week_diet = serializers.IntegerField(source='week_diet.id')
    weight = serializers.FloatField()

    
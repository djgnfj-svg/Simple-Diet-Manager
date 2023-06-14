from rest_framework import serializers

from accounts.models import BodyInfoRecord


# 몸무게와 그의 식단들의 id를 리턴해야한다.
class UserProfileSerializer(serializers.Serializer):
    week_diet = serializers.IntegerField(source='week_diet.id')
    weight = serializers.FloatField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        dt = obj.created_at.date()

        # '22년도 11월 3주차'로 변환
        week_number = (dt.day - 1) // 7 + 1
        formatted_date = "{:02d}년도 {:02d}월 {}주차".format(dt.year % 100, dt.month, week_number)

        return formatted_date
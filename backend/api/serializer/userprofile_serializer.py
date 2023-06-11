from rest_framework import serializers
from accounts.models import BodyInfoRecord

from meals.models import Meal


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyInfoRecord
        fields = '__all__'
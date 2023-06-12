from rest_framework import serializers

from accounts.models import BodyInfoRecord


class UserProfileSerializer(serializers.Serializer):
    class Meta:
        model = BodyInfoRecord
        fields = '__all__'

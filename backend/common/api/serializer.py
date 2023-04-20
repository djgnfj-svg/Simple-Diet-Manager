from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Base serializer for all models
    """
    def __init__(self, *args, **kwargs):
        super(BaseSerializer, self).__init__(*args, **kwargs)
        self.fields['created_at'].read_only = True
        self.fields['updated_at'].read_only = True

    class Meta:
        model = None
        fields = '__all__'
        exclude = ('created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
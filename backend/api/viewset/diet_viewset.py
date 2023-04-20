from rest_framework import viewsets

from api.serializer.diet_serializer import DietSerializer
from diets.models import Diet


class DietViewset(viewsets.ModelViewSet):
    serializer_class = DietSerializer
    queryset = Diet.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
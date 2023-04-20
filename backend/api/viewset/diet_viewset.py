from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.serializer.diet_serializer import DietMakeSerializer, DietSerializer
from api.serializer.purchase_serializer import WeekDietPurchaseSerializer
from common.message import error_msg
from diets.models import Diet, WeekDiet


class DietViewset(viewsets.ModelViewSet):
    serializer_class = DietSerializer
    queryset = Diet.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DietMakeViewset(viewsets.ViewSet):
    serializer_class = DietMakeSerializer

    def create(self, request):
        serializer = DietMakeSerializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(serializer.data)
            return Response(rtn, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        weekdiet = get_object_or_404(WeekDiet, pk=pk)
        serializer = WeekDietPurchaseSerializer(weekdiet)
        return Response(serializer.data, status=status.HTTP_200_OK)
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.serializer.diet_serializer import WeekDietMakeSerializer
from api.serializer.purchase_serializer import WeekDietPurchaseSerializer

from common.message import error_msg

from diets.models import WeekDiet


class WeekDietViewSet(viewsets.ViewSet):
    serializer_class = WeekDietMakeSerializer

    def create(self, request):
        user = JWTAuthentication().authenticate(request)

        serializer = WeekDietMakeSerializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(serializer.data, user)
            return Response(rtn, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        weekdiet = get_object_or_404(WeekDiet, pk=pk)
        serializer = WeekDietPurchaseSerializer(weekdiet)
        return Response(serializer.data, status=status.HTTP_200_OK)
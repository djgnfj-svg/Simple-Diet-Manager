from rest_framework import status, viewsets
from rest_framework.response import Response

from food.models import CookingOption, FoodCategory, Food

from api.Serializer.FoodSerializer import FoodSerializer, CookingOptionSerializer, FoodCategorySerializer


class CookingOptionViewset(viewsets.ModelViewSet):
    serializer_class = CookingOptionSerializer
    queryset = CookingOption.objects.order_by("-id")

class FoodCategoryViewset(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer
    queryset = FoodCategory.objects.order_by("-id")

class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.order_by("-id")
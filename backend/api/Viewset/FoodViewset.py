from rest_framework import status, viewsets
from rest_framework.response import Response
from Utils.functions.nutrient_utils import make_nutrient
from meals.MealManager import MealMakeManager

from foods.models import CookingOption, FoodCategory, Food

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        _food = Food.objects.get(id=serializer.data.get("id"))
        for kcal in range(400, 1500, 100):
            min, max = make_nutrient(kcal)
            makemanager = MealMakeManager()
            makemanager.make_meal(min, max, _food)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
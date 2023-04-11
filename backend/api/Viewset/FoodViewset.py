from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser
from Utils.functions.nutrient_utils import make_nutrient
from meals.MealManager import MealMakeManager

from foods.models import CookingOption, FoodCategory, Food

from api.Serializer.FoodSerializer import FoodSerializer, CookingOptionSerializer, FoodCategorySerializer


class CookingOptionViewset(viewsets.ModelViewSet):
    serializer_class = CookingOptionSerializer
    queryset = CookingOption.objects.order_by("-id")
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAdminUser]

# 
class FoodCategoryViewset(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer
    queryset = FoodCategory.objects.order_by("-id")
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAdminUser]


class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.order_by("-id")
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAdminUser]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            _food = Food.objects.get(id = serializer.data.get("id"))
            if Food.objects.count() > 20:
                makemanager = MealMakeManager()
                makemanager.meke_meal_range(300, 1200, 100, _food)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
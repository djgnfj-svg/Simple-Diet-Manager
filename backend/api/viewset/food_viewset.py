from rest_framework import status, viewsets
from rest_framework.response import Response

from api.serializer.food_serializer import (CookingOptionSerializer,
                                            FoodCategorySerializer,
                                            FoodSerializer)
from common.manager.meal_manager import MealManager
from foods.models import CookingOption, Food, FoodCategory


class CookingOptionViewset(viewsets.ModelViewSet):
    serializer_class = CookingOptionSerializer
    queryset = CookingOption.objects.order_by("-id")


class FoodCategoryViewset(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer
    queryset = FoodCategory.objects.order_by("-id")

class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', '')
        filtered_foods = Food.objects.filter(name__icontains=search)
        page = self.paginate_queryset(filtered_foods)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            _food = Food.objects.get(id=serializer.data.get("id"))
            if Food.objects.count() > 20:
                makemanager = MealManager()
                makemanager.meke_meal_range(300, 1200, 100, _food, bulk_create=True)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

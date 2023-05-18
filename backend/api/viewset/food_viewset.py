from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.serializer.food_serializer import (FoodCategorySerializer,
                                            FoodSerializer)
from common.geter.meal_getter import MealGetter
from common.maker.meal_maker import MealMaker
from foods.models import Food, FoodCategory
from meals.models import Meal


class FoodCategoryViewset(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer
    queryset = FoodCategory.objects.order_by("-id")

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = FoodCategory.objects.order_by("-id").exclude(name="기타")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.order_by("-id")

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        search = request.query_params.get('search', '')
        filtered_foods = Food.objects.filter(name__icontains=search).order_by("-id")

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
                makemanager = MealMaker(Meal)
                makemanager.meke_meal_range(300, 1200, 100, _food, bulk_create=True)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

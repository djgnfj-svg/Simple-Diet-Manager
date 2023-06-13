from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import status, viewsets
from rest_framework.response import Response

from api.serializer.food_serializer import FoodCategorySerializer, FoodSerializer
from common.maker.meal_maker import MealMaker

from foods.models import Food, FoodCategory
from meals.models import Meal


class FoodCategoryViewset(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        return FoodCategory.objects.order_by("-id").exclude(name="기타")

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    def get_queryset(self):
        search = self.request.query_params.get('search', '')
        return Food.objects.filter(name__icontains=search).order_by("-id")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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

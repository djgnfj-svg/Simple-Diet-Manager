from rest_framework import viewsets

from meals.models import Meal

from api.serializer.meal_serializer import MealSerializer


class MealViewset(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all().order_by('-id')

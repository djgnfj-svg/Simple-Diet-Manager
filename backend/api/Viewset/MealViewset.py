from rest_framework import viewsets

from api.Serializer.MealSerializer import MealSerializer

from meals.models import Meal


class MealViewset(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

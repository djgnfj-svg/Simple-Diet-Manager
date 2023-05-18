from rest_framework import routers

from api.viewset.diet_viewset import DietViewset
from api.viewset.food_viewset import FoodCategoryViewset, FoodViewset
from api.viewset.meal_viewset import MealViewset
from api.viewset.week_diet_viewset import WeekDietViewSet

router = routers.DefaultRouter()
router.register(r'diets', DietViewset, basename="diets")
router.register(r'week-diets', WeekDietViewSet, basename="week-diet")
router.register(r'foods', FoodViewset, basename="food")
router.register(r'food-category', FoodCategoryViewset, basename="food-category")
router.register(r'meals', MealViewset, basename="meals")
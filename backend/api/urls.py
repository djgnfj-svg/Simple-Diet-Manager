from rest_framework import routers

from api.viewset.diet_viewset import DietMakeViewset, DietViewset
from api.viewset.food_viewset import (CookingOptionViewset,
                                      FoodCategoryViewset, FoodViewset)
from api.viewset.meal_viewset import MealViewset

router = routers.DefaultRouter()
router.register(r'diets', DietViewset, basename="diets")
router.register(r'week-diets', DietMakeViewset, basename="week-diet")
router.register(r'foods', FoodViewset, basename="food")
router.register(r'food-category', FoodCategoryViewset, basename="food-category")
router.register(r'cooking-options', CookingOptionViewset, basename="cookingoptions")
router.register(r'meals', MealViewset, basename="meals")
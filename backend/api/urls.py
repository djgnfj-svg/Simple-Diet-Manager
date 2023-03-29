from rest_framework import routers
from api.Viewset.DietViewset import DietMakeViewset, DietViewset
from api.Viewset.FoodViewset import CookingOptionViewset, FoodCategoryViewset, FoodViewset
from api.Viewset.MealViewset import MealViewset

router = routers.DefaultRouter()
router.register(r'diets', DietViewset, basename="diet")
router.register(r'week-diets', DietMakeViewset, basename="diet")
router.register(r'foods', FoodViewset, basename="food")
router.register(r'food-category', FoodCategoryViewset, basename="food-category")
router.register(r'cooking-options', CookingOptionViewset, basename="cookingoptions")
router.register(r'meals', MealViewset, basename="diet")
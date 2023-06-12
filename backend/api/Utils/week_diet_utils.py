from common.geter.weekdiet_getter import WeekDietGetter

from foods.models import FoodCategory


def make_week_diet(userbodyinfo, validated_data, min_nutrient, max_nutrient):
    week_diet_manager = WeekDietGetter()
    categories = FoodCategory.objects.filter(id__in=validated_data["categories"])
    week_diet = week_diet_manager.get_data(
        validated_data["meal_count"], 
        userbodyinfo, min_nutrient, 
        max_nutrient, categories
        )
    
    return week_diet
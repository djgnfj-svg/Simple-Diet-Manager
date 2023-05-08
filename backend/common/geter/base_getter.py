from abc import abstractmethod

from django.db.models import Q

from common.base_manager import ManagerBase


class GetterBase(ManagerBase):
    def __init__(self, _model):
        super().__init__(_model)

    @abstractmethod
    def get_data(self):
        pass

    def find_instance(self, model, model_prefix, min_nutrient, max_nutrient, meal_count=None):
        q = Q()
        for nutrient in ["kcal", "protein", "fat", "carbs"]:
            nutrient_min = "{}{}".format(model_prefix, nutrient)
            nutrient_max = "{}{}".format(model_prefix, nutrient)
            q &= Q(**{"{}__gte".format(nutrient_min): min_nutrient[nutrient], "{}__lte".format(nutrient_max): max_nutrient[nutrient]})
            
            if meal_count is not None:
                q &= Q(meal_count=meal_count)
        return model.objects.filter(q)
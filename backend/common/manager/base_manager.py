from abc import *

from django.db.models import Q

# class ManagerBase(metaclass=ABCMeta):
#     pass
    

# class Manager(ManagerBase):
#     pass
    

# class MakeManager(Manager):
#     pass
    
# class GetManager(Manager):
#     pass

# class APIManager(ManagerBase):
# 아마 로그처럼 띄윚 않을까 싶다.
#     pass

class ManagerBase(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

class DietManagerBase(ManagerBase):
    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        pass
    
    def find_instance(self, model, model_prefix, min_nutrient, max_nutrient):
        q = Q()
        for nutrient in ["kcal", "protein", "fat", "carbs"]:
            nutrient_min = "{}{}".format(model_prefix, nutrient)
            nutrient_max = "{}{}".format(model_prefix, nutrient)
            q &= Q(**{"{}__gte".format(nutrient_min): min_nutrient[nutrient], "{}__lte".format(nutrient_max): max_nutrient[nutrient]})
        return model.objects.filter(q)

    def make_instance(self):
        pass
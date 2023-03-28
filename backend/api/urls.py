from rest_framework import routers
from api.Viewset.DietViewset import Diet_Make_Viewset

router = routers.DefaultRouter()
router.register(r'diets', Diet_Make_Viewset, basename="diet")
from rest_framework import routers
from api.Viewset.DietViewset import Diet_Viewset

router = routers.DefaultRouter()
router.register(r'diets', Diet_Viewset, basename="diet")
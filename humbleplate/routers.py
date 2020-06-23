from rest_framework import routers
from foods.viewsets import FoodViewSet

router = routers.DefaultRouter()

router.register(r'foods', FoodViewSet)
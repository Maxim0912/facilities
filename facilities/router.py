from rest_framework import routers

from dish.views import IngredientViewSet, DishViewSet
from restaurant.views import RestaurantViewSet
from user.views import UserViewSet


router = routers.DefaultRouter()
router.register('dish', DishViewSet)
router.register('inredient', IngredientViewSet)
router.register('restaurants', RestaurantViewSet)
router.register('users', UserViewSet)

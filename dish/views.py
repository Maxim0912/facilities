from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Dish, Ingredient
from .serializers import DishSerializer, IngredientSerializer


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class IngredientViewSet(ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

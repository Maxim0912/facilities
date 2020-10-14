from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Ingredient, Dish


class DishSerializer(ModelSerializer):
    """сумма калорий доступна только для чтения"""
    calories = ReadOnlyField()

    class Meta:
        model = Dish
        fields = '__all__'


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

from rest_framework.serializers import ModelSerializer, ReadOnlyField

from restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):
    """Владельца заведения можно получить только для чтения id """
    owner = ReadOnlyField(source='owner.id')

    class Meta:
        model = Restaurant
        fields = '__all__'

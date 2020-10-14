from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from restaurant.models import Restaurant


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        restaurant = PrimaryKeyRelatedField(many=True,
                                            queryset=Restaurant.objects.all())
        fields = ('id', 'username', 'password')

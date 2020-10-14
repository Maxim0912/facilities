from rest_framework.viewsets import ModelViewSet

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

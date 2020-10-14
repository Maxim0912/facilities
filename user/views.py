from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User

from .serializers import UserSerializer


class UserViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

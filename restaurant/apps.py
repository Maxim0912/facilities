from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    name = 'restaurant'

    def ready(self):
        from .signals import coordinates, avg

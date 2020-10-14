from django.apps import AppConfig


class DishConfig(AppConfig):
    name = 'dish'

    def ready(self):
        from .signals import ingredients_changed

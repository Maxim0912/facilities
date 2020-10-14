import os
from django.db.models import Avg
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from yandex_geocoder import Client

from .models import Restaurant
from dish.models import Dish


@receiver(pre_save, sender=Restaurant)
def coordinates(sender, instance, **kwargs):
    """Получение координат заведения через Геокодер API Яндекс"""
    client = Client(os.getenv('CLIENT_KEY'))
    if instance.address:
        instance.longitude, instance.latitude\
            = client.coordinates(instance.address)


@receiver(post_save, sender=Dish)
def avg(instance, **kwargs):
    """Рассчет средней стоимости блюд в заведении"""
    single_restaurant = Restaurant.objects.get(dish=instance)
    price = single_restaurant.dish.all().aggregate(Avg('price'))
    single_restaurant.avg_price = price.get('price__avg')
    single_restaurant.save()

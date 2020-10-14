import os
from django.db.models import Sum
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Dish


@receiver(m2m_changed, sender=Dish.ingredients.through)
def ingredients_changed(sender, instance, action, **kwargs):
    """при изменении состава блюда(ингредиентов), меняется сумма калорий"""
    if action == "post_add":
        calory_dish = instance.ingredients.all().aggregate(Sum('calory'))
        instance.calories = calory_dish.get('calory__sum')
        instance.save()
        print(os.getenv('VAR3'))

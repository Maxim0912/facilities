from django.db import models

from restaurant.models import Restaurant


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    calory = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static')
    calories = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    restaurant = models.ForeignKey(Restaurant, related_name='dish',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name

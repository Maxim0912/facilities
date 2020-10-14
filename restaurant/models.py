from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static', blank=True)
    opened_time = models.TimeField()
    closed_time = models.TimeField()

    address = models.CharField(max_length=100)
    longitude = models.CharField(max_length=30, default=None)
    latitude = models.CharField(max_length=30, default=None)
    avg_price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    owner = models.ForeignKey(User, related_name='restaurant',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Vehicle(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

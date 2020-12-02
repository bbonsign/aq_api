from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.


class Parameter(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    preferred_unit = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}: {self.preferred_unit}"


class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=2, default='US')

    def __str__(self):
        return f"{self.name}, {self.country}"


class Location(models.Model):
    city = models.ForeignKey(
        to='City', on_delete=CASCADE, related_name='locations')
    name = models.CharField(max_length=256)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.name}, {self.city}"


class Measurement(models.Model):
    location = models.ForeignKey(
        to='Location', on_delete=CASCADE, related_name='measurements')
    parameter = models.ForeignKey(
        to='Parameter', on_delete=CASCADE, related_name='measurements')
    value = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.location.city}: {self.value} {self.parameter.preferred_unit}"

from django.db import models
from .choices import TRANSMISSION_CHOICES, BODYTYPE_CHOICES, ENEGY_SOURCE_CHOICES

class Manufacturer(models.Model):
    name = models.CharField(max_length= 20, unique=True)
    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length = 20)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    transmission = models.CharField(
        max_length=120,
        choices=TRANSMISSION_CHOICES,
    )
    body_type = models.CharField(
        max_length=120, 
        choices=BODYTYPE_CHOICES,
    )
    doors = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    odo = models.PositiveIntegerField()
    fuel_rate = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    safety_rate = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    fuel_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    color = models.CharField(max_length=20)
    energy_source = models.CharField(
        max_length=20,
        choices = ENEGY_SOURCE_CHOICES,
    )
    engine_size = models.PositiveIntegerField()
    features = models.ManyToManyField(Feature, related_name="cars", blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url
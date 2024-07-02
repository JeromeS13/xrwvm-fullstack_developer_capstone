from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):

    TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        ('crossover', 'Crossover'),
        ('convertible', 'Convertible')
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    year = models.IntegerField(default=2024,
                               validators=[
                                   MaxValueValidator(2024),
                                   MinValueValidator(2016)
                               ])
    vin = models.CharField(max_length=100)
    dealer_id = models.IntegerField(default=0,
                                    validators=[
                                        MinValueValidator(0)
                                    ])

    def __str__(self):
        return str(self.year) + " " + \
            str(self.car_make) + " " + \
            self.name + " " + \
            self.type
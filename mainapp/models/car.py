from django.db import models


class Car(models.Model):
    class EngineTypes(models.TextChoices):
        GAS = 'g', 'Gas engine'
        DIESEL = 'd', 'Diesel engine'
        ELECTRIC = 'e', 'Electric engine'

    TRANSMISSION_TYPES = (
        ('A', 'Automatic'),
        ('M', 'Manual')
    )

    manufacturer = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    engine_type = models.CharField(max_length=20, choices=EngineTypes.choices, default=EngineTypes.GAS)
    engine_power = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=64, choices=TRANSMISSION_TYPES, default='M')
    color = models.CharField(max_length=64)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

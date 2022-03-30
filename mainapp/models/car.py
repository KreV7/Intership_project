from django.db import models

from core.enums import (
    TransmissionTypes,
    EngineTypes
)


class Car(models.Model):

    manufacturer = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    engine_type = models.CharField(max_length=20, choices=EngineTypes.choices(), default=EngineTypes.GAS)
    engine_power = models.PositiveIntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=64, choices=TransmissionTypes.choices(), default=TransmissionTypes.M)
    color = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.manufacturer} {self.car_model} [{self.engine_type}{self.engine_power}{self.transmission}]'

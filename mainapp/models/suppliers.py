from decimal import Decimal

from django.db import models

from .car import Car


class Supplier(models.Model):
    title = models.CharField(max_length=128)
    year_foundation = models.DateField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.year_foundation.year})'


class SuppliersGarage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car} ({self.supplier}): {self.price}$'


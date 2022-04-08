from decimal import Decimal

from django.core import validators
from django.db import models
from core import BaseSalesModel
from .car import Car


class Supplier(models.Model):
    title = models.CharField(max_length=128)
    year_foundation = models.DateField()
    number_of_cars = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(default=0, validators=[validators.MaxValueValidator(100)])
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

    # def __str__(self):
    #     return f'{self.car} ({self.supplier}): {self.price}$'


class SuppliersSales(BaseSalesModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    car = models.ForeignKey(SuppliersGarage, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.supplier.title}: Discount {self.discount}% on {self.car}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.car in self.supplier.suppliersgarage_set.all():
            super(SuppliersSales, self).save()
        else:
            raise Exception(f"Choose a car from the {self.supplier} garage")

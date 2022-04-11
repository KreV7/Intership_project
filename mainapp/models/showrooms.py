from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from core import BaseSalesModel
from .suppliers import Supplier, SuppliersGarage
from .customers import AdvUser


class Showroom(models.Model):
    title = models.CharField(max_length=256)
    location = CountryField()
    parameters_car = models.JSONField(
        default=dict(
            manufacturer='',
            car_model='',
            engine_type='',
            engine_power='',
            transmission='',
            color=''
        )
    )
    cash_balance = models.DecimalField(max_digits=25, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.location})'

    @property
    def bought_cars(self):
        return self.suppliersaleshistory_set.aggregate(num_cars=Sum('quantity'))['num_cars']

    @property
    def bought_cars_by_supplier(self):
        return self.suppliersaleshistory_set.values('supplier').annotate(num_cars=Sum('quantity'))

    @property
    def spent_money(self):
        return self.suppliersaleshistory_set.aggregate(spent=Sum('total_price'))['spent']

    @property
    def sold_cars(self):
        return self.showroomcustomerhistory_set.aggregate(num_cars=Sum('quantity'))['num_cars']

    @property
    def received_money(self):
        return self.showroomcustomerhistory_set.aggregate(received=Sum('total_cost'))['received']

    @property
    def unique_customer(self):
        return len(self.showroomcustomerhistory_set.values('customer'))


class ShowroomsGarage(models.Model):
    car = models.ForeignKey(SuppliersGarage, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=25, decimal_places=2, default=Decimal('0.00'))
    quantity = models.PositiveIntegerField(default=1)
    selling_price = models.DecimalField(max_digits=25, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f'{self.car} ({self.showroom})'


class ShowroomCustomerHistory(models.Model):
    customer = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    car = models.ForeignKey(ShowroomsGarage, on_delete=models.CASCADE)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=25, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}: {self.car} ({self.showroom}) - {self.quantity} - {self.total_cost}'


class SupplierSalesHistory(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    car = models.ForeignKey(SuppliersGarage, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=25, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.supplier}: {self.showroom} -> {self.car}'


class ShowroomsSales(BaseSalesModel):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    car = models.ForeignKey(ShowroomsGarage, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.showroom}: Discount {self.discount} on {self.car}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.car in self.showroom.showroomsgarage_set.all():
            super(ShowroomsSales, self).save()
        else:
            raise Exception(f"Choose a car from the {self.showroom} garage")

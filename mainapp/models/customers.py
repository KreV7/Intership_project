from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class AdvUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=True)
    cash_balance = models.DecimalField(max_digits=25, decimal_places=2, default=Decimal('0.00'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.user.username})'

    @property
    def bought_cars(self):
        return self.showroomcustomerhistory_set.aggregate(num_cars=Sum('quantity'))['num_cars']

    @property
    def spent_money(self):
        return self.showroomcustomerhistory_set.aggregate(spent=Sum('total_cost'))['spent']

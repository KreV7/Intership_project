import datetime

from django.db import models
from django.core import validators


class BaseSalesModel(models.Model):
    discount = models.PositiveIntegerField(validators=[validators.MaxValueValidator(100)])
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=7)))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

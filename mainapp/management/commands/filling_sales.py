import random

from django.core.management.base import BaseCommand

from mainapp.models import (
    Supplier,
    SuppliersGarage,
    SuppliersSales,
    Showroom,
    ShowroomsSales,
    ShowroomsGarage,
)


class Command(BaseCommand):
    help = 'Filling in database supplier and showrooms discounts'

    def handle(self, *args, **options):

        """Clearing database for sales"""

        SuppliersSales.objects.all().delete()
        ShowroomsSales.objects.all().delete()

        """Filling suppliers discounts"""

        suppliers = Supplier.objects.all()

        for supplier in suppliers:
            supplier_cars = random.sample(
                list(SuppliersGarage.objects.filter(supplier=supplier)),
                random.randint(1, len(SuppliersGarage.objects.filter(supplier=supplier)))
            )
            for car in supplier_cars:
                SuppliersSales.objects.create(
                    discount=random.randint(10, 40),
                    supplier=supplier,
                    car=car
                )

        """Filling suppliers discounts"""

        showrooms = Showroom.objects.all()

        for showroom in showrooms:
            if len(ShowroomsGarage.objects.filter(showroom=showroom)) > 1:
                showroom_cars = random.sample(
                    list(ShowroomsGarage.objects.filter(showroom=showroom)),
                    random.randint(1, len(ShowroomsGarage.objects.filter(showroom=showroom)))
                )
                for car in showroom_cars:
                    ShowroomsSales.objects.create(
                        discount=random.randint(10, 25),
                        showroom=showroom,
                        car=car
                    )

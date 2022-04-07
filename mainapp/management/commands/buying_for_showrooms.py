import random
from decimal import Decimal

from django.core.management.base import BaseCommand

from mainapp.models import (
    Showroom,
    ShowroomsGarage,
    SuppliersGarage,
    SupplierSalesHistory,
)


class Command(BaseCommand):
    help = 'Clearing Showrooms garage and next buying cars for showrooms'

    def handle(self, *args, **options):
        """Clearing showrooms garages"""

        ShowroomsGarage.objects.all().delete()
        SupplierSalesHistory.objects.all().delete()

        """Buying cars for showrooms"""

        showrooms = Showroom.objects.all()

        for showroom in showrooms:
            cars = SuppliersGarage.objects.select_related('car').filter(
                car__manufacturer__in=showroom.parameters_car['manufacturer'],
                car__car_model__in=showroom.parameters_car['car_model'],
                car__engine_type__in=showroom.parameters_car['engine_type'],
                car__engine_power__in=showroom.parameters_car['engine_power'],
                car__transmission__in=showroom.parameters_car['transmission'],
                car__color__in=showroom.parameters_car['color']
            )
            if cars:
                number_of_cars = random.randint(10, 25)
                for _ in range(number_of_cars):
                    car = random.choice(cars)
                    showroom_cars = [car.car for car in ShowroomsGarage.objects.filter(showroom=showroom)]
                    if car in showroom_cars:
                        get_car = ShowroomsGarage.objects.get(showroom=showroom, car=car)
                        get_car.quantity += 1
                        get_car.save()
                    else:
                        ShowroomsGarage.objects.create(
                            car=car,
                            supplier=car.supplier,
                            showroom=showroom,
                            purchase_price=car.price,
                            quantity=1,
                            selling_price=car.price * Decimal("1.2"),
                        )
                    SupplierSalesHistory.objects.create(
                        showroom=showroom,
                        car=car,
                        supplier=car.supplier,
                        price=car.price,
                        total_price=car.price
                    )

import datetime
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from django_countries import data as countries_data

from mainapp.models import (
    AdvUser,
    Car,
    Supplier,
    SuppliersGarage,
    Showroom
)

from core.enums import (
    CARS,
    ENGINE_POWER,
    TransmissionTypes,
    EngineTypes,
    Colors
)


class Command(BaseCommand):
    help = 'Filling database random datas'

    def handle(self, *args, **options):
        """Clearing database"""
        User.objects.filter(is_superuser=False).delete()
        AdvUser.objects.all().delete()
        Car.objects.all().delete()
        Supplier.objects.all().delete()
        SuppliersGarage.objects.all().delete()

        fake = Faker()

        """Filling random users"""
        users_count = 10

        for _ in range(users_count):
            u = User.objects.create_user(username=fake.simple_profile()['username'],
                                         email=fake.email(),
                                         password='asd123zxc',
                                         first_name=fake.first_name(),
                                         last_name=fake.last_name())
            AdvUser.objects.create(user=u, phone=fake.phone_number(), cash_balance=random.randint(15000, 100000))

        """Filling random cars"""
        if Car.objects.all().count() == 0:
            car_count = 50
            for _ in range(car_count):
                rand_car = random.choice(list(CARS.keys()))
                rand_model = random.choice(CARS[rand_car])
                Car.objects.create(manufacturer=rand_car,
                                   car_model=rand_model,
                                   engine_type=random.choice(EngineTypes.choices())[0],
                                   engine_power=random.choice(ENGINE_POWER),
                                   transmission=random.choice(TransmissionTypes.choices())[0],
                                   color=random.choice(Colors.choices())[0],
                                   description=fake.text())

        """Filling random Suppliers"""

        suppliers_count = 25
        if Supplier.objects.all().count() == 0:
            for _ in range(suppliers_count):
                Supplier.objects.create(title=fake.company(),
                                        year_foundation=datetime.datetime(random.randint(1950, 2015), 1, 1))

        """Filling suppliers garage"""

        suppliers = Supplier.objects.all()
        cars = Car.objects.all()
        for supplier in suppliers:
            car_count_in_garage = random.randint(15, 40)
            for _ in range(car_count_in_garage):
                SuppliersGarage.objects.create(car=random.choice(cars),
                                               supplier=supplier,
                                               price=random.randint(8000, 50000))

        """Filling random showrooms"""

        showrooms_count = 25
        for _ in range(showrooms_count):
            Showroom.objects.create(title=fake.company(),
                                    location=random.choice(list(countries_data.COUNTRIES.keys())),
                                    cash_balance=random.randint(500000, 1500000))

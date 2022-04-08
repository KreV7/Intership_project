import datetime
import random

from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from django_countries import data as countries_data

from mainapp.models import (
    AdvUser,
    Car,
    Supplier,
    SuppliersGarage,
    Showroom,
)
from core import CARS, ENGINE_POWER
from core.enums import (
    TransmissionTypes,
    EngineTypes,
    Colors
)


class Command(BaseCommand):
    help = 'Filling database random datas'

    def handle(self, *args, **options):
        # Clearing database
        User.objects.filter(is_superuser=False).delete()
        AdvUser.objects.all().delete()
        Car.objects.all().delete()
        Supplier.objects.all().delete()
        Showroom.objects.all().delete()

        fake = Faker()

        # Filling random users
        users_count = 25

        for _ in range(users_count):
            u = User.objects.create_user(username=fake.simple_profile()['username'],
                                         email=fake.email(),
                                         password='asd123zxc',
                                         first_name=fake.first_name(),
                                         last_name=fake.last_name())
            AdvUser.objects.create(user=u, phone=fake.phone_number(), cash_balance=random.randint(35000, 100000))

        # Filling random cars

        for car_man in CARS.keys():
            for car_model in CARS[car_man]:
                for _ in range(5):
                    Car.objects.create(manufacturer=car_man,
                                       car_model=car_model,
                                       engine_type=random.choice(EngineTypes.choices())[0],
                                       engine_power=random.choice(ENGINE_POWER),
                                       transmission=random.choice(TransmissionTypes.choices())[0],
                                       color=random.choice(Colors.choices())[0],
                                       description=fake.text())

        # Filling random Suppliers

        suppliers_count = 15

        for _ in range(suppliers_count):
            Supplier.objects.create(title=fake.company(),
                                    year_foundation=datetime.datetime(random.randint(1950, 2015), 1, 1),
                                    number_of_cars=random.randint(10, 25),
                                    discount=random.randint(10, 30))

        # Filling suppliers garage

        cars = Car.objects.all()

        for car in cars:
            car_price = random.randint(10000, 50000)
            suppliers = random.sample(list(Supplier.objects.all()), 5)
            for supplier in suppliers:
                SuppliersGarage.objects.create(
                    car=car,
                    supplier=supplier,
                    price=Decimal(round(random.uniform(car_price * 0.8, car_price * 1.2), 2)).quantize(Decimal('1.00')),
                )

        # Filling random showrooms

        showrooms_count = 25

        for _ in range(showrooms_count):
            manufacturers = random.sample(list(CARS.keys()), 3)
            car_models = [random.sample(CARS[model], random.randint(1, len(CARS[model]))) for model in
                          manufacturers]
            new_car_models = [m for lst in car_models for m in lst]
            Showroom.objects.create(title=fake.company(),
                                    location=random.choice(list(countries_data.COUNTRIES.keys())),
                                    parameters_car={
                                        'manufacturer': manufacturers,
                                        'car_model': new_car_models,
                                        'engine_type': [et[0] for et in
                                                        random.sample(EngineTypes.choices(), random.randint(1, 3))],
                                        'engine_power': random.sample(ENGINE_POWER,
                                                                      random.randint(1, len(ENGINE_POWER))),
                                        'transmission': [tr[0] for tr in random.sample(TransmissionTypes.choices(),
                                                                                       random.randint(1, 2))],
                                        'color': [color[0] for color in random.sample(
                                            Colors.choices(),
                                            random.randint(3, len(Colors.choices()))
                                        )]

                                    },
                                    cash_balance=random.randint(500000, 1500000))


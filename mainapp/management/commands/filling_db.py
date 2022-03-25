import datetime
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from django_countries import data as countries_data

from mainapp.models import AdvUser, Car, Supplier, SuppliersGarage, Showroom


class Command(BaseCommand):
    help = 'Filling database random datas'

    def handle(self, *args, **options):
        fake = Faker()
        """Filling random users"""
        User.objects.filter(is_superuser=False).delete()
        AdvUser.objects.all().delete()

        users_count = 10

        for _ in range(users_count):
            u = User.objects.create_user(username=fake.simple_profile()['username'],
                                         email=fake.email(),
                                         password='asd123zxc',
                                         first_name=fake.first_name(),
                                         last_name=fake.last_name())
            AdvUser.objects.create(user=u, phone=fake.phone_number())

        """Filling random cars"""
        if Car.objects.all().count() == 0:
            car_count = 50
            ENGINE_TYPE = ['g', 'd', 'e']
            ENGINE_POWER = [1200, 1400, 1500, 1800, 2000, 2400]
            TRANSMISSION = ['A', 'M']
            COLOR = ['white', 'red', 'black', 'green', 'pink', 'orange', 'yellow', 'purple', 'grey', 'blue']
            CARS = {'Audi': ['A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q3', 'Q5', 'Q7', 'Q8'],
                    'BMW': ['2 серия', '3 серия', '4 серия', '5 серия', '6 серия', '7 серия', '8 серия', 'i3', 'iX',
                            'X1',
                            'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'Z4'],
                    'Cadillac': ['XT6'],
                    'Changan': ['CS35 Plus', 'CS55', 'CS75 FL'],
                    'Chery': ['Tiggo 4', 'Tiggo 7 Pro', 'Tiggo 8', 'Tiggo 8 Pro'],
                    'Chevrolet': ['Cobalt', 'Nexia', 'Spark'],
                    'Citroen': ['Berlingo', 'C3 Aircross', 'C4', 'C5 Aircross', 'SpaceTourer'],
                    'Geely': ['Atlas Pro', 'Coolray', 'Tugella'],
                    'Great Wall': ['GWM Poer'],
                    'Haval': ['F7', 'F7 X', 'H9', 'Jolion'],
                    'Hyundai': ['Accent', 'Creta', 'Palisade', 'Santa Fe', 'Sonata', 'Tucson'],
                    'Jeep': ['Compass', 'Grand Cherokee', 'Renegade', 'Wrangler'],
                    'Kia': ['Rio', 'Seltos', 'Sorento', 'Sportage'],
                    'LADA (ВАЗ)': ['Granta', 'Largus', 'Niva Legend', 'Niva Travel', 'Vesta', 'XRAY '],
                    'Lexus': ['ES', 'GX', 'LC', 'LS', 'LX', 'NX', 'RX', 'UX'],
                    'Maserati': ['Levante'],
                    'MINI': ['Countryman', 'Hatch'],
                    'Nissan': ['Murano', 'Qashqai', 'Terrano', 'X-Trail'],
                    'Opel': ['Astra', 'Combo Cargo', 'Combo Life', 'Corsa', 'Crossland', 'Grandland X', 'Insignia',
                             'Vivaro', 'Zafira Life'],
                    'Peugeot': ['2008', '3008', '408', '5008', 'Boxer', 'Expert', 'Partner', 'Traveller'],
                    'Subaru': ['Forester', 'Outback', 'XV'],
                    'Tesla': ['Model 3', 'Model S', 'Model X'],
                    'Toyota': ['Alphard', 'C-HR', 'Camry', 'Corolla', 'Fortuner', 'Highlander', 'Hilux', 'Land Cruiser',
                               'Land Cruiser Prado', 'RAV4'],
                    'Volkswagen': ['Polo', 'Taos', 'Tiguan'],
                    'Volvo': ['S60', 'S90', 'V60', 'V90', 'XC40', 'XC60', 'XC90'],
                    'УАЗ': ['Hunter', 'Patriot', 'Pickup']}
            for _ in range(car_count):
                rand_car = random.choice(list(CARS.keys()))
                rand_model = random.choice(CARS[rand_car])
                Car.objects.create(manufacturer=rand_car,
                                   car_model=rand_model,
                                   engine_type=random.choice(ENGINE_TYPE),
                                   engine_power=random.choice(ENGINE_POWER),
                                   transmission=random.choice(TRANSMISSION),
                                   color=random.choice(COLOR),
                                   description=fake.text())

        """Filling random Suppliers"""

        suppliers_count = 25
        if Supplier.objects.all().count() == 0:
            for _ in range(suppliers_count):
                Supplier.objects.create(title=fake.company(),
                                        year_foundation=datetime.datetime(random.randint(1950, 2015), 1, 1))

        """Filling suppliers garage"""

        if SuppliersGarage.objects.all().count() == 0:
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
        if Showroom.objects.all().count() == 0:
            for _ in range(showrooms_count):
                Showroom.objects.create(title=fake.company(),
                                        location=random.choice(list(countries_data.COUNTRIES.keys())),
                                        cash_balance=random.randint(250000, 1500000))

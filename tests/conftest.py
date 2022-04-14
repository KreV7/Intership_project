import random
import pytest
import datetime

from decimal import Decimal

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django_countries import data as countries_data

from core import ENGINE_POWER, CARS
from core.enums import EngineTypes, TransmissionTypes, Colors
from mainapp.models import (
    Car,
    AdvUser,
    Supplier,
    SuppliersGarage,
    SuppliersSales,
    SupplierSalesHistory,
    Showroom,
    ShowroomsGarage,
    ShowroomsSales,
    ShowroomCustomerHistory,
)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create(
        username='test_user',
        password='asd123zxc',
        email='test_user@admin.com',
        first_name='Test',
        last_name='User'
    )
    return user


@pytest.fixture
def adv_user(user):
    adv_user = AdvUser.objects.create(
        user=user,
        phone='+375(29)111-11-11',
        cash_balance=Decimal('0.00'),
    )
    return adv_user


@pytest.fixture
def car():
    car = Car.objects.create(
        manufacturer='Audi',
        car_model='Q3',
        engine_type='GAS',
        engine_power=1800,
        transmission='A',
        color='GREY',
        description=''
    )

    return car


@pytest.fixture
def cars():
    count = 5
    for _ in range(count):
        Car.objects.create(
            manufacturer=random.choice(list(CARS.keys())),
            car_model=random.choice(CARS[random.choice(list(CARS.keys()))]),
            engine_type=random.choice(EngineTypes.choices())[0],
            engine_power=random.choice(ENGINE_POWER),
            transmission=random.choice(TransmissionTypes.choices())[0],
            color=random.choice(Colors.choices())[0],
            description=""
        )
    cars = Car.objects.all()
    return cars


@pytest.fixture
def supplier():
    supplier = Supplier.objects.create(
        title='First Supplier Company',
        year_foundation=datetime.date.today(),
        number_of_cars=random.randint(15, 25),
        discount=random.randint(0, 80)
    )
    return supplier


@pytest.fixture
def suppliers():
    count = 5
    for num in range(count):
        Supplier.objects.create(
            title=f'{num} Supplier Company',
            year_foundation=datetime.date.today(),
            number_of_cars=random.randint(15, 25),
            discount=random.randint(0, 80)
        )
    suppliers = Supplier.objects.all()
    return suppliers


@pytest.fixture
def suppliers_garage(supplier, cars):
    for car in cars:
        SuppliersGarage.objects.create(
            car=car,
            supplier=supplier,
            price=random.randint(10000, 50000)
        )
    suppliers_garage = SuppliersGarage.objects.all()
    return suppliers_garage


@pytest.fixture
def supplier_sale(suppliers_garage):
    rand_car_in_suppliers_garage = random.choice(suppliers_garage)
    supplier_sale = SuppliersSales.objects.create(
        discount=random.randint(1, 80),
        supplier=rand_car_in_suppliers_garage.supplier,
        car=rand_car_in_suppliers_garage,
    )
    return supplier_sale


@pytest.fixture
def showroom():
    showroom = Showroom.objects.create(
        title='First Cars Dealer',
        location=random.choice(list(countries_data.COUNTRIES.keys())),
        parameters_car={
            'manufacturer': [],
            'car_model': [],
            'engine_type': [],
            'engine_power': [],
            'transmission': [],
            'color': []
        },
        cash_balance=random.randint(500000, 1500000)
    )
    return showroom


@pytest.fixture
def showrooms():
    count = 5
    for num in range(count):
        Showroom.objects.create(
            title=f'{num} Cars Dealer',
            location=random.choice(list(countries_data.COUNTRIES.keys())),
            parameters_car={
                'manufacturer': [],
                'car_model': [],
                'engine_type': [],
                'engine_power': [],
                'transmission': [],
                'color': []
            },
            cash_balance=random.randint(500000, 1500000)
        )
    showrooms = Showroom.objects.all()
    return showrooms


@pytest.fixture
def showrooms_garage(suppliers_garage, showroom):
    for car in suppliers_garage:
        ShowroomsGarage.objects.create(
            car=car,
            supplier=car.supplier,
            showroom=showroom,
            purchase_price=car.price,
            quantity=1,
            selling_price=car.price * Decimal("1.2")
        )
    showrooms_garage = ShowroomsGarage.objects.all()
    return showrooms_garage


@pytest.fixture
def showroom_sale(showrooms_garage):
    rand_car_in_showroom_garage = random.choice(showrooms_garage)
    showroom_sale = ShowroomsSales.objects.create(
        discount=random.randint(1, 80),
        showroom=rand_car_in_showroom_garage.showroom,
        car=rand_car_in_showroom_garage,
    )
    return showroom_sale


@pytest.fixture
def supplier_sales_history(showrooms, suppliers_garage):
    for showroom in showrooms:
        for supp_car in suppliers_garage:
            SupplierSalesHistory.objects.create(
                showroom=showroom,
                car=supp_car,
                supplier=supp_car.supplier,
                price=supp_car.price,
                quantity=1,
                total_price=supp_car.price * 1
            )
    supplier_sales_history = SupplierSalesHistory.objects.all()
    return supplier_sales_history


@pytest.fixture
def showroom_customer_history(adv_user, showrooms_garage):
    for car in showrooms_garage:
        ShowroomCustomerHistory.objects.create(
            customer=adv_user,
            car=car,
            showroom=car.showroom,
            price=car.selling_price,
            quantity=1,
            total_cost=car.selling_price * 1
        )
    showroom_customer_history = ShowroomCustomerHistory.objects.all()
    return showroom_customer_history

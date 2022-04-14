import datetime
import random

import pytest

from mainapp.models import Supplier, SuppliersGarage

pytestmark = pytest.mark.django_db


def test_create_supplier(client):
    payload = dict(
        title='First Supplier Company',
        year_foundation=datetime.date.today(),
        number_of_cars=random.randint(15, 25),
        discount=random.randint(0, 80)
    )

    resp = client.post('/suppliers/', data=payload)

    assert resp.data['title'] == payload['title']
    assert resp.data['year_foundation'] == payload['year_foundation'].strftime('%Y-%m-%d')
    assert resp.data['number_of_cars'] == payload['number_of_cars']
    assert resp.data['discount'] == payload['discount']
    assert resp.status_code == 201


def test_suppliers_list(client, suppliers):
    resp = client.get('/suppliers/')

    assert len(resp.data) == 5
    assert resp.status_code == 200


def test_supplier_detail(client, suppliers):
    supplier = random.choice(suppliers)

    resp = client.get(f'/suppliers/{supplier.id}/')

    assert resp.data['title'] == supplier.title
    assert resp.data['year_foundation'] == supplier.year_foundation.strftime('%Y-%m-%d')
    assert resp.data['number_of_cars'] == supplier.number_of_cars
    assert resp.data['discount'] == supplier.discount
    assert resp.status_code == 200


def test_supplier_put(client, suppliers):
    supplier = random.choice(suppliers)

    payload = dict(
        title='First Supplier Company',
        year_foundation=datetime.date.today(),
        number_of_cars=random.randint(15, 25),
        discount=random.randint(0, 80)
    )

    resp = client.put(f'/suppliers/{supplier.id}/', data=payload)

    assert resp.data['title'] == payload['title']
    assert resp.data['year_foundation'] == payload['year_foundation'].strftime('%Y-%m-%d')
    assert resp.data['number_of_cars'] == payload['number_of_cars']
    assert resp.data['discount'] == payload['discount']
    assert resp.status_code == 200


def test_supplier_delete(client, suppliers):
    supplier = random.choice(suppliers)

    resp = client.delete(f'/suppliers/{supplier.id}/')

    assert resp.status_code == 204
    assert Supplier.objects.all().count() == 4


def test_create_suppliers_garage(client, suppliers, cars):
    supplier = random.choice(suppliers)
    car = random.choice(cars)

    payload = dict(
        car=car.id,
        supplier=supplier.id,
        price=random.randint(10000, 50000),
    )

    resp = client.post('/suppliers_garage/', payload)

    assert resp.data['car'] == payload['car']
    assert resp.data['supplier'] == payload['supplier']
    assert int(float(resp.data['price'])) == payload['price']
    assert resp.status_code == 201


def test_suppliers_garage_list(client, suppliers_garage):
    resp = client.get('/suppliers_garage/')

    assert len(resp.data) == 5
    assert resp.status_code == 200


def test_supplier_garage_put(client, suppliers_garage, cars, suppliers):
    car = random.choice(cars)
    supplier = random.choice(suppliers)
    rand_car_in_suppliers_garage = random.choice(suppliers_garage)

    payload = dict(
        car=car.id,
        supplier=supplier.id,
        price=random.randint(10000, 50000),
    )

    resp = client.put(f'/suppliers_garage/{rand_car_in_suppliers_garage.id}/', payload)

    assert resp.data['id'] == rand_car_in_suppliers_garage.id
    assert resp.data['car'] == payload['car']
    assert resp.data['supplier'] == payload['supplier']
    assert int(float(resp.data['price'])) == payload['price']
    assert resp.status_code == 200


def test_suppliers_garage_delete(client, suppliers_garage):
    rand_car_in_suppliers_garage = random.choice(suppliers_garage)

    resp = client.delete(f'/suppliers_garage/{rand_car_in_suppliers_garage.id}/')

    assert resp.status_code == 204
    assert SuppliersGarage.objects.all().count() == 4

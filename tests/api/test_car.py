import random

import pytest

from mainapp.models import Car

pytestmark = pytest.mark.django_db


def test_create_car(client):
    payload = dict(
        manufacturer='Audi',
        car_model='A6',
        engine_type='GAS',
        engine_power=1200,
        transmission='A',
        color='BLACK',
        description='',
    )
    resp = client.post('/cars/', payload)

    assert resp.data['manufacturer'] == payload['manufacturer']
    assert resp.data['engine_power'] == payload['engine_power']
    assert resp.status_code == 201


def test_cars_list(client, cars):
    resp = client.get('/cars/')

    assert len(resp.data) == 5
    assert resp.status_code == 200


def test_car_detail(client, cars):
    car = random.choice(cars)
    resp = client.get(f'/cars/{car.id}/')

    assert resp.data['manufacturer'] == car.manufacturer
    assert resp.data['car_model'] == car.car_model
    assert resp.data['engine_type'] == car.engine_type
    assert resp.data['engine_power'] == car.engine_power
    assert resp.data['transmission'] == car.transmission
    assert resp.data['color'] == car.color
    assert resp.data['description'] == car.description
    assert resp.status_code == 200


def test_car_put(client, cars):
    car = random.choice(cars)
    payload = dict(
        manufacturer='BMV',
        car_model='Serial 5',
        engine_type='GAS',
        engine_power=2500,
        transmission='A',
        color='PINK',
        description='',
    )
    resp = client.put(f'/cars/{car.id}/', payload)

    assert resp.data['manufacturer'] == payload['manufacturer']
    assert resp.data['car_model'] == payload['car_model']
    assert resp.data['engine_type'] == payload['engine_type']
    assert resp.data['engine_power'] == payload['engine_power']
    assert resp.data['transmission'] == payload['transmission']
    assert resp.data['color'] == payload['color']
    assert resp.data['description'] == payload['description']
    assert resp.status_code == 200


def test_car_delete(client, cars):
    car = random.choice(cars)

    resp = client.delete(f'/cars/{car.id}/')

    assert resp.status_code == 204
    assert Car.objects.all().count() == 4

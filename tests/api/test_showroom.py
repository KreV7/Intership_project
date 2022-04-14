import random
import pytest

from django_countries import data as countries_data

from mainapp.models import Showroom

pytestmark = pytest.mark.django_db


def test_create_showroom(client):
    payload = dict(
        title='First Cars Dealer',
        location=random.choice(list(countries_data.COUNTRIES.keys())),
        cash_balance=random.randint(500000, 1500000)
    )

    resp = client.post('/showrooms/', data=payload)

    assert resp.data['title'] == payload['title']
    assert resp.data['location'] == payload['location']
    assert int(float(resp.data['cash_balance'])) == payload['cash_balance']
    assert resp.status_code == 201


def test_showrooms_list(client, showrooms):
    resp = client.get('/showrooms/')

    assert len(resp.data) == 5
    assert resp.status_code == 200


def test_showroom_detail(client, showrooms):
    showroom = random.choice(showrooms)

    resp = client.get(f'/showrooms/{showroom.id}/')

    print(resp.data['parameters_car'])

    assert resp.data['title'] == showroom.title
    assert resp.data['location'] == showroom.location
    assert int(float(resp.data['cash_balance'])) == showroom.cash_balance
    assert resp.data['parameters_car'] == showroom.parameters_car
    assert resp.status_code == 200


def test_showroom_put(client, showrooms):
    showroom = random.choice(showrooms)

    payload = dict(
        title='First Cars Dealer',
        location=random.choice(list(countries_data.COUNTRIES.keys())),
        cash_balance=random.randint(500000, 1500000)
    )

    resp = client.put(f'/showrooms/{showroom.id}/', data=payload)

    assert resp.data['title'] == payload['title']
    assert resp.data['location'] == payload['location']
    assert int(float(resp.data['cash_balance'])) == payload['cash_balance']
    assert resp.status_code == 200


def test_showroom_delete(client, showrooms):
    showroom = random.choice(showrooms)

    resp = client.delete(f'/showrooms/{showroom.id}/')

    assert resp.status_code == 204
    assert Showroom.objects.all().count() == 4


def test_statistic_showrooms(client, supplier_sales_history):

    resp = client.get('/statistic/showrooms/')

    assert len(resp.data) == 5
    assert resp.status_code == 200


def test_statistic_showroom(client, supplier_sales_history):
    rand_showroom = random.choice(supplier_sales_history).showroom

    resp = client.get(f'/statistic/showrooms/{rand_showroom.id}/')

    assert resp.data['bought_cars'] == rand_showroom.bought_cars
    assert int(float(resp.data['spent_money'])) == rand_showroom.spent_money
    assert resp.data['sold_cars'] == rand_showroom.sold_cars
    assert resp.data['received_money'] == rand_showroom.received_money
    assert resp.data['unique_customer'] == rand_showroom.unique_customer
    assert resp.data['bought_cars_by_supplier'][0] == rand_showroom.bought_cars_by_supplier[0]
    assert resp.status_code == 200

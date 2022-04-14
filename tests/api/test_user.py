import pytest

pytestmark = pytest.mark.django_db


def test_create_user(client):
    payload = {
        'email': 'neos7@tut.by',
        'username': 'neos7',
        'password': 'asd123zxc',
    }

    resp = client.post('/auth/users/', data=payload)

    data = resp.data

    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert 'password' not in data
    assert resp.status_code == 201


def test_user_me(client, user):
    client.force_authenticate(user=user)
    resp = client.get('/auth/users/me/')
    data = resp.data

    assert data['username'] == user.username
    assert data['id'] == user.id
    assert resp.status_code == 200


def test_statistic_advusers(client, showroom_customer_history):
    resp = client.get('/statistic/users/')

    assert len(resp.data) == 1
    assert resp.status_code == 200


def test_statistic_advuser(client, showroom_customer_history):
    advuser = showroom_customer_history[0].customer

    resp = client.get(f'/statistic/users/{advuser.id}/')

    assert resp.data['bought_cars'] == advuser.bought_cars
    assert resp.data['spent_money'] == advuser.spent_money
    assert resp.status_code == 200

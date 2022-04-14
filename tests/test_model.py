import random
import pytest

from decimal import Decimal

from core.enums import EngineTypes, TransmissionTypes, Colors

pytestmark = pytest.mark.django_db


def test_user_model(user):
    assert user._meta.get_field('username').max_length == 150
    assert user._meta.get_field('username').unique is True
    assert user._meta.get_field('first_name').max_length == 150
    assert user._meta.get_field('last_name').max_length == 150
    assert user._meta.get_field('is_active').default is True


def test_advuser_model(adv_user):
    assert adv_user._meta.get_field('phone').max_length == 50
    assert adv_user._meta.get_field('phone').blank is True
    assert adv_user._meta.get_field('cash_balance').max_digits == 25
    assert adv_user._meta.get_field('cash_balance').decimal_places == 2
    assert adv_user._meta.get_field('cash_balance').default == Decimal('0.00')
    assert adv_user._meta.get_field('created').auto_now_add is True
    assert adv_user._meta.get_field('updated').auto_now is True
    assert str(adv_user) == f'{adv_user.user.get_full_name()} ({adv_user.user.username})'


def test_car_model(car):
    assert car._meta.get_field('manufacturer').max_length == 128
    assert car._meta.get_field('car_model').max_length == 128
    assert car._meta.get_field('engine_type').max_length == 128
    assert car._meta.get_field('engine_type').choices == EngineTypes.choices()
    assert car._meta.get_field('engine_type').default == EngineTypes.GAS
    assert car._meta.get_field('engine_power').blank is True
    assert car._meta.get_field('engine_power').null is True
    assert car._meta.get_field('transmission').max_length == 64
    assert car._meta.get_field('transmission').choices == TransmissionTypes.choices()
    assert car._meta.get_field('transmission').default == TransmissionTypes.M.value
    assert car._meta.get_field('color').max_length == 64
    assert car._meta.get_field('color').choices == Colors.choices()
    assert car._meta.get_field('description').blank is True
    assert car._meta.get_field('description').default == ''
    assert car._meta.get_field('is_active').default is True
    assert car._meta.get_field('created').auto_now_add is True
    assert car._meta.get_field('updated').auto_now is True
    assert str(car) == f'{car.manufacturer} {car.car_model} [{car.engine_type}{car.engine_power}{car.transmission}]'


def test_supplier_model(supplier):
    assert supplier._meta.get_field('title').max_length == 128
    assert supplier._meta.get_field('number_of_cars').blank is True
    assert supplier._meta.get_field('number_of_cars').null is True
    assert supplier._meta.get_field('discount').default == 0
    assert supplier._meta.get_field('is_active').default is True
    assert supplier._meta.get_field('created').auto_now_add is True
    assert supplier._meta.get_field('updated').auto_now is True
    assert str(supplier) == f'{supplier.title} ({supplier.year_foundation.year})'


def test_supplier_sale_model(supplier_sale):
    assert str(supplier_sale) == f'{supplier_sale.supplier.title}: ' \
                                 f'Discount {supplier_sale.discount}% on {supplier_sale.car}'


def test_showrooms_model(showroom):
    assert str(showroom) == f'{showroom.title} ({showroom.location})'


def test_showroom_sale_model(showroom_sale):
    assert str(showroom_sale) == f'{showroom_sale.showroom}: Discount {showroom_sale.discount} on {showroom_sale.car}'


def test_supplier_sales_history_model(supplier_sales_history):
    rand_choice = random.choice(supplier_sales_history)

    assert str(rand_choice) == f'{rand_choice.supplier}: {rand_choice.showroom} -> {rand_choice.car}'


def test_showroom_customer_history_model(showroom_customer_history):
    rand_choice = random.choice(showroom_customer_history)

    assert str(rand_choice) == f'{rand_choice.customer}: {rand_choice.car} ' \
                               f'({rand_choice.showroom}) - {rand_choice.quantity} - {rand_choice.total_cost}'

import decimal
import random

from Intership_project.celery import app
from .models import (
    AdvUser,
    Showroom,
    ShowroomsGarage,
    ShowroomsSales,
    ShowroomCustomerHistory,
    SuppliersGarage,
    SupplierSalesHistory,
    SuppliersSales,
    Supplier,
)


@app.task
def buy_car_showroom_supplier():
    """Purchase for each showroom of one random car selected according to the parameters of this showroom"""

    showrooms = Showroom.objects.all()

    for showroom in showrooms:
        """Filtering cars for each showroom by parameters car"""
        cars = SuppliersGarage.objects.select_related('car').filter(
            car__manufacturer__in=showroom.parameters_car['manufacturer'],
            car__car_model__in=showroom.parameters_car['car_model'],
            car__engine_type__in=showroom.parameters_car['engine_type'],
            car__engine_power__in=showroom.parameters_car['engine_power'],
            car__transmission__in=showroom.parameters_car['transmission'],
            car__color__in=showroom.parameters_car['color']
        )
        if cars:
            """Random choice one car for buying"""
            random_car = random.choice(cars)
            price_by_suppliers = {}

            """Finding all proposals by all suppliers"""
            cars_by_suppliers = SuppliersGarage.objects.filter(car=random_car.car)

            if cars_by_suppliers:

                """Count of purchased cars for each supplier and writing to dictionary"""
                for car in cars_by_suppliers:
                    count_sold_cars = SupplierSalesHistory.objects.filter(
                        showroom=showroom,
                        supplier=car.supplier
                    ).count()
                    price_by_suppliers[car.supplier.id] = [car, count_sold_cars]
                """Finding discounts by suppliers and if we have discounts adding their to dictionary"""

                sales_for_car = SuppliersSales.objects.filter(car=random_car).all()
                if sales_for_car:
                    for sale in sales_for_car:
                        price_by_suppliers[sale.supplier.id].append(sale.discount)

                """Finding discounts by loyalty program"""
                for k, v in price_by_suppliers.items():
                    supplier = Supplier.objects.get(id=k)
                    if v[1] >= supplier.number_of_cars:
                        price_by_suppliers[k].append(supplier.discount)
                """Determination of the price taking into account the discount"""

                price_by_suppliers_with_discount = {}
                for k, v in price_by_suppliers.items():
                    if len(v) == 2:
                        price_by_suppliers_with_discount[k] = [v[0], v[0].price]
                    elif len(v) == 3:
                        price_by_suppliers_with_discount[k] = [v[0],
                                                               v[0].price * decimal.Decimal(str((100 - v[2]) / 100))]
                    elif len(v) == 4:
                        price_by_suppliers_with_discount[k] = [v[0], v[0].price * decimal.Decimal(
                            str((100 - v[2] - v[3]) / 100))]

                """Finding the best price"""
                min_price = ['car', 1000000]
                for k, v in price_by_suppliers_with_discount.items():
                    if v[1] < min_price[1]:
                        min_price[0] = v[0]
                        min_price[1] = v[1]

                """Buying a car"""
                buying_car = min_price[0]
                car_price = min_price[1]
                quantity = random.randint(1, 3)
                if showroom.cash_balance > car_price * quantity:
                    showroom_cars = [car.car for car in ShowroomsGarage.objects.filter(showroom=showroom)]
                    if buying_car in showroom_cars:
                        get_exist_car = ShowroomsGarage.objects.get(showroom=showroom, car=buying_car)
                        get_exist_car.quantity += quantity
                        get_exist_car.save()
                    else:
                        ShowroomsGarage.objects.create(
                            car=buying_car,
                            supplier=buying_car.supplier,
                            showroom=showroom,
                            purchase_price=car_price,
                            quantity=quantity,
                            selling_price=car_price * decimal.Decimal('1.2')
                        )
                    showroom.cash_balance -= car_price * quantity
                    showroom.save()

                    """Writing history for purchase car from supplier to showroom"""
                    SupplierSalesHistory.objects.create(
                        showroom=showroom,
                        car=buying_car,
                        supplier=buying_car.supplier,
                        price=car_price,
                        quantity=quantity,
                        total_price=car_price * quantity
                    )


@app.task
def buy_car_customer_supplier():
    """Task for a random customer to buy a random car"""

    """Choosing random customer for purchase"""
    customer = random.choice(AdvUser.objects.all())

    """Choosing random car for purchase"""
    random_car = random.choice(ShowroomsGarage.objects.all())

    """Finding all proposals by showrooms"""
    proposals_car = ShowroomsGarage.objects.filter(car=random_car.car)
    list_cars = []

    """Checking discount on cars"""
    for discount_car in proposals_car:
        discount = ShowroomsSales.objects.filter(car=discount_car).first()
        if discount:
            list_cars.append(
                [discount_car, discount_car.selling_price * decimal.Decimal(str((100 - discount.discount) / 100))]
            )
        else:
            list_cars.append([discount_car, discount_car.selling_price])

    """Finding the best price"""
    min_price = ['car', 1000000]
    for car in list_cars:
        if car[1] < min_price[1]:
            min_price[0] = car[0]
            min_price[1] = car[1]

    """Buying a car"""
    car = min_price[0]
    car_price = min_price[1]
    quantity = 1
    if customer.cash_balance > car_price * quantity:
        ShowroomCustomerHistory.objects.create(
            customer=customer,
            car=car,
            showroom=car.showroom,
            price=car_price,
            quantity=quantity,
            total_cost=car_price * quantity
        )
        customer.cash_balance -= car_price * quantity
        customer.save()
        showroom = Showroom.objects.get(id=car.showroom.id)
        showroom.cash_balance += car_price * quantity
        showroom.save()
    else:
        customer.cash_balance += random.randint(5000, 25000)

    return f'\n{customer.user.username} bought {car.car.car}: {car_price}$'

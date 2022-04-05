import decimal
import random

from Intership_project.celery import app
from .models import (
    AdvUser,
    Showroom,
    ShowroomsGarage,
    SuppliersGarage,
    SupplierSalesHistory,
    ShowroomCustomerHistory
)


@app.task
def buy_car_showroom_supplier():
    showroom = random.choice(Showroom.objects.all())
    supplier_car = random.choice(SuppliersGarage.objects.all())
    if showroom.cash_balance > supplier_car.price:
        sold_car = ShowroomsGarage.objects.create(
            car=supplier_car,
            supplier=supplier_car.supplier,
            showroom=showroom,
            purchase_price=supplier_car.price,
            quantity=1,
            selling_price=supplier_car.price * decimal.Decimal("1.2"),
        )
        sold_car.save()
        SupplierSalesHistory.objects.create(
            showroom=showroom,
            car=supplier_car,
            supplier=sold_car.supplier,
            price=sold_car.purchase_price,
            quantity=sold_car.quantity,
            total_price=sold_car.purchase_price * sold_car.quantity
        )
        showroom.cash_balance -= sold_car.purchase_price * sold_car.quantity
    else:
        showroom.cash_balance += random.randint(250000, 1000000)


@app.task
def buy_car_customer_supplier():
    customer = random.choice(AdvUser.objects.all())
    showroom_car = random.choice(ShowroomsGarage.objects.all())
    if customer.cash_balance >= showroom_car.selling_price:
        ShowroomCustomerHistory.objects.create(
            customer=customer,
            car=showroom_car,
            showroom=showroom_car.showroom,
            price=showroom_car.selling_price,
            quantity=1,
            total_cost=showroom_car.selling_price * 1
        )
        customer.cash_balance -= showroom_car.selling_price * 1
        showroom_car.cash_balance += showroom_car.selling_price * 1
        if showroom_car.quantity == 1:
            showroom_car.delete()
        else:
            showroom_car.quantity -= 1
    else:
        customer.cash_balance += random.randint(5000, 25000)

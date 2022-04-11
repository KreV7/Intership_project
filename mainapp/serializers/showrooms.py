from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from mainapp.models import Showroom, ShowroomsGarage
from mainapp.serializers import SupplierGarageShowroomsGarageSerializer, SupplierSerializer


class ShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = (
            'id',
            'title',
            'location',
            'parameters_car',
            'cash_balance'
        )


class ShowroomsGarageSerializer(serializers.ModelSerializer):
    car = SupplierGarageShowroomsGarageSerializer()
    supplier = SupplierSerializer()
    showroom = ShowroomSerializer()

    class Meta:
        model = ShowroomsGarage
        fields = (
            'id',
            'car',
            'supplier',
            'showroom',
            'purchase_price',
            'quantity',
            'selling_price',
        )


class ShowroomsStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = (
            'id',
            'title',
            'bought_cars',
            'spent_money',
            'sold_cars',
            'received_money',
            'unique_customer',
            'bought_cars_by_supplier',
        )

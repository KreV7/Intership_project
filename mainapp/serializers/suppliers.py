from rest_framework import serializers

from mainapp.models import Supplier, SuppliersGarage, SuppliersSales
from mainapp.serializers import CarSerializer


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'id',
            'title',
            'year_foundation',
            'number_of_cars',
            'discount',
        )


class SuppliersGarageSerializer(serializers.ModelSerializer):
    # car = CarSerializer()
    # supplier = SupplierSerializer()

    class Meta:
        model = SuppliersGarage
        fields = (
            'id',
            'car',
            'supplier',
            'price'
        )


class SupplierGarageShowroomsGarageSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = SuppliersGarage
        fields = (
            'id',
            'car',
            'price'
        )


class SupplierStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'id',
            'title',
            'sold_cars',
            'received_money'
        )


class SuppliersSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliersSales
        fields = (
            'id',
            'supplier',
            'car',
            'discount',
            'start_date',
            'end_date',
        )

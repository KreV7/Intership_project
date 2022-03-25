from rest_framework import serializers
from django.contrib.auth.models import User
from django_countries.serializers import CountryFieldMixin
from mainapp.models import AdvUser, Car, Showroom, ShowroomsGarage, ShowroomCustomerHistory, \
    Supplier, SuppliersGarage, SupplierSalesHistory


class AdvUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = ['phone',
                  'cash_balance']


class UserSerializers(serializers.ModelSerializer):
    advuser = AdvUserSerializer()

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'advuser']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id',
                  'manufacturer',
                  'car_model',
                  'engine_type',
                  'engine_power',
                  'transmission',
                  'color',
                  'description']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id',
                  'title',
                  'year_foundation']


class SuppliersGarageSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = SuppliersGarage
        fields = ['id',
                  'car',
                  'supplier',
                  'price']


class SupplierGarageShowroomsGarageSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = SuppliersGarage
        fields = ['id',
                  'car',
                  'price']


class ShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ['id',
                  'title',
                  'location',
                  'parameters_car',
                  'cash_balance']


class ShowroomsGarageSerializer(serializers.ModelSerializer):
    car = SupplierGarageShowroomsGarageSerializer()
    supplier = SupplierSerializer()
    showroom = ShowroomSerializer()

    class Meta:
        model = ShowroomsGarage
        fields = ['id',
                  'car',
                  'supplier',
                  'showroom',
                  'purchase_price',
                  'quantity',
                  'selling_price']


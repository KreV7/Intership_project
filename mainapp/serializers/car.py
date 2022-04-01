from rest_framework import serializers

from mainapp.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'manufacturer',
            'car_model',
            'engine_type',
            'engine_power',
            'transmission',
            'color',
            'description'
        )

import django_filters
from django_filters import rest_framework as filters
from django_filters.widgets import BooleanWidget

from mainapp.models import Car, Supplier, Showroom
from core.enums import (
    TransmissionTypes,
    EngineTypes
)


class CarFilter(filters.FilterSet):
    manufacturer = django_filters.CharFilter(lookup_expr='iexact')
    transmission = django_filters.ChoiceFilter(choices=TransmissionTypes.choices)
    engine_type = django_filters.ChoiceFilter(choices=EngineTypes.choices)

    class Meta:
        model = Car
        fields = (
            'manufacturer',
            'transmission',
            'engine_type'
        )


class SuppliersFilter(filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    year_foundation = django_filters.DateFilter()

    class Meta:
        model = Supplier
        fields = (
            'title',
            'year_foundation'
        )


class ShowroomsFilter(filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    location = django_filters.CharFilter(lookup_expr='iexact')
    is_active = django_filters.BooleanFilter(widget=BooleanWidget())

    class Meta:
        model = Showroom
        fields = (
            'title',
            'location',
            'is_active'
        )

from rest_framework import viewsets, mixins, permissions
from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response

from mainapp.filtersets import (
    CarFilter,
    SuppliersFilter,
    ShowroomsFilter
)

from mainapp.models import (
    AdvUser,
    Car,
    Showroom,
    ShowroomsGarage,
    ShowroomsSales,
    Supplier,
    SuppliersGarage,
    SuppliersSales,
)
from mainapp.serializers import (
    MyUserSerializer,
    UsersStatisticSerializer,
    CarSerializer,
    SupplierSerializer,
    SuppliersGarageSerializer,
    SupplierStatisticSerializer,
    SuppliersSalesSerializer,
    ShowroomSerializer,
    ShowroomsGarageSerializer,
    ShowroomsStatisticSerializer,
    ShowroomsSalesSerializer,
)


class UserReadOnlyViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = User.objects.select_related('advuser').all()
    serializer_class = MyUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(id=user.id)


class UsersStatisticViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = AdvUser.objects.select_related('user').all()
    serializer_class = UsersStatisticSerializer


class CarAdminViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarFilter


class CarViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset = Car.objects.all()


class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SuppliersFilter


class SuppliersGarageViewSet(viewsets.ModelViewSet):
    queryset = SuppliersGarage.objects.all()
    serializer_class = SuppliersGarageSerializer


class SuppliersStatisticViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierStatisticSerializer


class SuppliersSalesViewSet(viewsets.ModelViewSet):
    queryset = SuppliersSales.objects.all()
    serializer_class = SuppliersSalesSerializer


class ShowroomsViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShowroomsFilter

    @action(detail=True, methods=['get'], url_path='garage')
    def showroom_garage(self, request, *args, **kwargs):
        garage = Showroom.objects.get(id=kwargs.get('pk')).showroomsgarage_set.all()
        garage = ShowroomsGarageSerializer(garage, many=True)
        return Response(garage.data)


class ShowroomsGarageViewSet(viewsets.ModelViewSet):
    queryset = ShowroomsGarage.objects.select_related('car').select_related('supplier').select_related('showroom').all()
    serializer_class = ShowroomsGarageSerializer


class ShowroomsStatisticViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomsStatisticSerializer


class ShowroomsSalesViewSet(viewsets.ModelViewSet):
    queryset = ShowroomsSales.objects.all()
    serializer_class = ShowroomsSalesSerializer

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainapp.views import (
    UserReadOnlyViewSet,
    UsersStatisticViewSet,
    CarAdminViewSet,
    SuppliersViewSet,
    SuppliersGarageViewSet,
    SuppliersStatisticViewSet,
    SuppliersSalesViewSet,
    ShowroomsViewSet,
    ShowroomsGarageViewSet,
    ShowroomsStatisticViewSet,
    ShowroomsSalesViewSet,
)

router = DefaultRouter()
router.register('users', UserReadOnlyViewSet, basename='UserReadOnlyViewSet')
router.register('cars', CarAdminViewSet, basename='CarViewSet')
router.register('suppliers', SuppliersViewSet, basename='SuppliersViewSet')
router.register('suppliers_garage', SuppliersGarageViewSet, basename='SuppliersGarageViewSet')
router.register('suppliers_sales', SuppliersSalesViewSet, basename='SuppliersSalesViewSet')
router.register('showrooms', ShowroomsViewSet, basename='ShowroomsViewSet')
router.register('showrooms_garage', ShowroomsGarageViewSet, basename='ShowroomsGarageViewSet')
router.register('showrooms_sales', ShowroomsSalesViewSet, basename='ShowroomsSalesViewSet')
router.register('statistic/users', UsersStatisticViewSet, basename='UsersStatisticViewSet')
router.register('statistic/suppliers', SuppliersStatisticViewSet, basename='SuppliersStatisticViewSet')
router.register('statistic/showrooms', ShowroomsStatisticViewSet, basename='ShowroomsStatisticViewSet')


urlpatterns = [
    path('', include(router.urls))
]

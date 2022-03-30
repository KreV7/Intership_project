from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainapp.views import UserReadOnlyViewSet, CarAdminViewSet, SuppliersViewSet, SuppliersGarageViewSet, ShowroomsViewSet, \
    ShowroomsGarageViewSet

router = DefaultRouter()
router.register('users', UserReadOnlyViewSet, basename='UserReadOnlyViewSet')
router.register('cars', CarAdminViewSet, basename='CarViewSet')
router.register('suppliers', SuppliersViewSet, basename='SuppliersViewSet')
router.register('suppliers_garage', SuppliersGarageViewSet, basename='SuppliersGarageViewSet')
router.register('showrooms', ShowroomsViewSet, basename='ShowroomsViewSet')
router.register('showrooms_garage', ShowroomsGarageViewSet, basename='ShowroomsGarageViewSet')

urlpatterns = [
    path('', include(router.urls))
]

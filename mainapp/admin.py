from django.contrib import admin

from mainapp.models import (
    Car,
    AdvUser,
    Showroom,
    ShowroomsGarage,
    ShowroomCustomerHistory,
    Supplier,
    SuppliersGarage,
    SupplierSalesHistory
)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer',
        'car_model',
        'engine_type',
        'engine_power',
        'transmission',
        'color',
        'description',
        'is_active'
    )
    list_filter = (
        'manufacturer',
        'car_model',
        'engine_type',
        'engine_power',
        'transmission',
        'color',
    )


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'cash_balance',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = (
        'title',
        'year_foundation',
        'is_active',
        'created',
        'updated'
    )
    date_hierarchy = 'year_foundation'


@admin.register(SuppliersGarage)
class SuppliersGarageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = (
        'car',
        'supplier',
        'price',
        'is_active',
        'created',
        'updated'
    )

    list_filter = (
        'car__manufacturer',
        'supplier',
        'is_active'
    )


@admin.register(SupplierSalesHistory)
class SupplierSalesHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = (
        'showroom',
        'car',
        'supplier',
        'price',
        'quantity',
        'total_price',
        'is_active'
    )
    list_filter = (
        'showroom',
        'car__car__manufacturer',
        'supplier'
    )


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'cash_balance',
        'is_active',
        'created',
    )
    list_filter = (
        'location',
        'is_active'
    )


@admin.register(ShowroomsGarage)
class ShowroomsGarageAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'showroom',
        'purchase_price',
        'quantity',
        'selling_price',
        'is_active',
        'created',
    )
    list_filter = (
        'car__car__manufacturer',
        'supplier',
        'showroom',
        'is_active'
    )


@admin.register(ShowroomCustomerHistory)
class ShowroomCustomerHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'car',
        'showroom',
        'price',
        'quantity',
        'total_cost',
        'is_active',
        'created'
    )
    list_filter = (
        'customer',
        'car__car__car__manufacturer',
        'showroom',
        'is_active'
    )

from django.contrib import admin

from mainapp.models import Car, AdvUser, Showroom, ShowroomsGarage, ShowroomCustomerHistory, Supplier, \
    SuppliersGarage, SupplierSalesHistory

admin.site.register(Car)
admin.site.register(AdvUser)
admin.site.register(Showroom)
admin.site.register(ShowroomsGarage)
admin.site.register(ShowroomCustomerHistory)
admin.site.register(Supplier)
admin.site.register(SuppliersGarage)
admin.site.register(SupplierSalesHistory)

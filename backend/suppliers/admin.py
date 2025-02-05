from django.contrib import admin
from suppliers.models import Supplier, SupplierRetailerMapping

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'owner_name', 'email', 'created_at')
    search_fields = ('company_name', 'owner_name', 'email')

@admin.register(SupplierRetailerMapping)
class SupplierRetailerMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'retailer')
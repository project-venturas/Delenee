from django.contrib import admin
from products.models import Product, Variant, PriceList

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'SKU', 'product', 'unit_type', 'unit_value', 'MOQ', 'created_at')
    search_fields = ('name', 'SKU')
    
@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'variant', 'buying_price', 'selling_price', 'created_at')

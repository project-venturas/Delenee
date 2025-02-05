from django.contrib import admin
from carts.models import Cart, CartItem
# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'retailer', 'supplier', 'created_at', 'last_modified_at')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'variant', 'price_list', 'quantity')
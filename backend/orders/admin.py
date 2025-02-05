from django.contrib import admin
from orders.models import Order, OrderItem

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'retailer', 'total_amount', 'order_status', 'created_at')
    list_filter = ('order_status',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product_name', 'SKU', 'quantity', 'price')
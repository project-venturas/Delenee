from django.db import models
from suppliers.models import Supplier

from retailers.models import Retailer

# Create your models here.
class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='orders')
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.IntegerField()
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)
    # Although the DBML indicates created_at as an integer, we use DateTimeField for timestamp data.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.order_status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=50)
    unit_value = models.IntegerField()
    SKU = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"
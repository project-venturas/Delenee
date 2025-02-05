from django.db import models
from suppliers.models import Supplier

from products.models import Product, Variant, PriceList

from retailers.models import Retailer


# Create your models here.
class Cart(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='carts')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)  # updated on each save

    def __str__(self):
        return f"Cart #{self.id} by {self.retailer.company_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='cart_items')
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
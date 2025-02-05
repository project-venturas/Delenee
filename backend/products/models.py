from django.db import models

from suppliers.models import Supplier

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# Create your models here.
class Variant(models.Model):
    # Define choices for unit_type based on your note.
    UNIT_TYPE_CHOICES = (
        ('grams', 'Grams'),
        ('kilograms', 'Kilograms'),
        ('liter', 'Liter'),
        ('milliliter', 'Milliliter'),
        # Add other unit types as needed
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    SKU = models.CharField(max_length=100, unique=True, help_text="Unique ID to identify the product")
    name = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=50, choices=UNIT_TYPE_CHOICES)
    unit_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    MOQ = models.IntegerField()

    def __str__(self):
        return self.name

class PriceList(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='price_lists')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='price_lists')
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PriceList: {self.variant.SKU} from {self.supplier.company_name}"
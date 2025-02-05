from django.db import models

# Create your models here.
class Inventory(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='inventories')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='inventories')
    available_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.variant.name} inventory for {self.supplier.company_name}"
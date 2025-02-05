from django.db import models
from address.models import Address
from retailers.models import Retailer


# Create your models here.
class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=50, null=True, blank=True)
    whatsapp_number = models.BigIntegerField()
    alternative_contact_number = models.BigIntegerField()
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='suppliers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    
class SupplierRetailerMapping(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='retailer_mappings')
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='supplier_mappings')

    class Meta:
        unique_together = ('supplier', 'retailer')
        verbose_name = "Supplier-Retailer Mapping"
        verbose_name_plural = "Supplier-Retailer Mappings"

    def __str__(self):
        return f"{self.supplier.company_name} ↔ {self.retailer.company_name}"

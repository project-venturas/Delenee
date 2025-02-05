from django.db import models

from address.models import Address

# Create your models here.
class Retailer(models.Model):
    company_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=50, null=True, blank=True)
    whatsapp_number = models.BigIntegerField()
    alternative_contact_number = models.BigIntegerField()
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='retailers', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
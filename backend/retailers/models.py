from django.db import models

# Create your models here.
class Retailer(models.Model):
    id = models.AutoField(primary_key=True,)
    company_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    gstin = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    alternative_contact_number = models.CharField(max_length=100)
    address_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # automatically set on creation

    def __str__(self):
        return self.address

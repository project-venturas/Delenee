from django.contrib import admin
from address.models import Address

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'city', 'state', 'pincode', 'created_at')
    search_fields = ('address', 'city', 'state')

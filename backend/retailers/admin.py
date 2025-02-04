from django.contrib import admin

from .models import Retailer
# Register your models here.

class RetailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'owner_name', 'gstin', 'whatsapp_number' )
    
admin.site.register(Retailer, RetailerAdmin)
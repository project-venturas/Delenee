from django.contrib import admin

from .models import Retailer
# Register your models here.

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'owner_name', 'email', 'created_at')
    search_fields = ('company_name', 'owner_name', 'email')
    
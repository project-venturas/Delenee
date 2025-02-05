from django.contrib import admin

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'variant', 'available_quantity', 'created_at', 'last_modified_at')
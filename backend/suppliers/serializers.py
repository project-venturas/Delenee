from rest_framework import serializers
from .models import Supplier, SupplierRetailerMapping

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
class SupplierRetailerMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierRetailerMapping
        fields = '__all__'
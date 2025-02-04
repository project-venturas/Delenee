from django.shortcuts import render

from rest_framework import viewsets
from .serializers import RetailerSerializer
from .models import Retailer

# Create your views here.
class RetailerViewset(viewsets.ModelViewSet):
    serializer_class = RetailerSerializer
    queryset = Retailer.objects.all()    
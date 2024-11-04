from django.shortcuts import render

# Create your views here.
# fleet/views.py

from rest_framework import viewsets
from .models import Tuktuk, Driver, Cashier
from .serializers import TuktukSerializer, DriverSerializer, CashierSerializer

class TuktukViewSet(viewsets.ModelViewSet):
    queryset = Tuktuk.objects.all()
    serializer_class = TuktukSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class CashierViewSet(viewsets.ModelViewSet):
    queryset = Cashier.objects.all()
    serializer_class = CashierSerializer

# fleet/serializers.py

from rest_framework import serializers
from .models import Tuktuk, Driver, Cashier

class TuktukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuktuk
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class CashierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashier
        fields = '__all__'

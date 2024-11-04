from django.db import models

# Create your models here.
# bookings/models.py

from django.db import models
from fleet.models import Tuktuk, Driver

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    cargo = models.TextField()
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_tuktuk = models.ForeignKey(Tuktuk, on_delete=models.CASCADE)
    assigned_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    booking_date = models.DateTimeField(auto_now_add=True)

    def calculate_cost(self):
        base_cost = 200
        additional_cost = max(0, self.distance_km - 1) * 50
        self.cost = base_cost + additional_cost
        self.save()

    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"

# bookings/models.py (continued for Payments)

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking}"

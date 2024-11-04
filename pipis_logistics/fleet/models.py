from django.db import models

# Create your models here.
# fleet/models.py

from django.db import models

class Tuktuk(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    mileage = models.IntegerField()
    capacity = models.DecimalField(max_digits=5, decimal_places=2)
    assigned_driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} - {self.model}"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    picture = models.ImageField(upload_to='drivers/')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=22000)

    def __str__(self):
        return self.name

class Cashier(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=25000)

    def __str__(self):
        return self.name

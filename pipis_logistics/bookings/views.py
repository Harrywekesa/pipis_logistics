from django.shortcuts import render

# Create your views here.
# bookings/views.py

from rest_framework import viewsets
from .models import Booking, Payment
from .serializers import BookingSerializer, PaymentSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        booking.calculate_cost()  # Calculate cost based on distance

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

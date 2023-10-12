# booking/models.py

from django.db import models
from user.models import User  # Import the User model from your user app

class Booking(models.Model):
    # Define fields for Booking model
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_as_rider')
    status = models.CharField(max_length=20)
    booking_time = models.DateTimeField(auto_now_add=True)
    cancel_time = models.DateTimeField(null=True, blank=True)

class Ride(models.Model):
    # Define fields for Ride model
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='bookings_as_ride')

class Payment(models.Model):
    # Define fields for Payment model
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")  # Add status field with a default value
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='bookings_as_payment')


    def __str__(self):
        return f"Payment for Ride {self.ride.id} - ${self.amount}"

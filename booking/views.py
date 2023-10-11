# booking/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, Payment, Ride
from .serializers import BookingSerializer, PaymentSerializer, RideSerializer
from django.utils import timezone
from rest_framework.decorators import action

class BookingView(APIView):
    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, booking_id, format=None):
        try:
            booking = Booking.objects.get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({"detail": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)

        if booking.status != "Canceled":
            booking.status = "Canceled"
            booking.cancel_time = timezone.now()
            booking.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Booking is already canceled."}, status=status.HTTP_400_BAD_REQUEST)

    def create_payment(self, request, booking_id, format=None):
        try:
            booking = Booking.objects.get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({"detail": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)

        if booking.payment:
            return Response({"detail": "Payment for this booking already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            booking.payment = payment
            booking.status = "Paid"
            booking.save()
            return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='create-ride')
    def create_ride(self, request, format=None):
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            ride = serializer.save()
            return Response(RideSerializer(ride).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

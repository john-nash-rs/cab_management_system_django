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

class PaymentView(APIView):

    def post(self, request, booking_id, format=None):
        try:
            booking = Booking.objects.get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({"detail": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)

        if booking.status == "Paid":
            return Response({"detail": "Payment for this booking already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            booking.status = "Paid"
            booking.save()
            payment = serializer.save()
            payment.booking = booking
            return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RideView(APIView):
    def post(self, request, format=None):
        # Create a new ride
        ride_serializer = RideSerializer(data=request.data)
        if ride_serializer.is_valid():
            ride = ride_serializer.save()

            # Update the associated booking's status to "Confirm"
            booking = ride.booking
            booking.status = "Confirm"
            booking.save()

            return Response({
                "ride": RideSerializer(ride).data,
                "booking": BookingSerializer(booking).data
            }, status=status.HTTP_201_CREATED)
        return Response(ride_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# booking/urls.py
from django.urls import path
from .views import BookingView, PaymentView, RideView

urlpatterns = [
    path('book/', BookingView.as_view(), name='booking'),
    path('ride/', RideView.as_view(), name='ride'),
    path('payment/<int:booking_id>/', PaymentView.as_view(), name='payment'),
]

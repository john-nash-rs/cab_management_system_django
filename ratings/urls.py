# ratings/urls.py

from django.urls import path
from .views import RatingCreate

urlpatterns = [
    path('create/', RatingCreate.as_view(), name='rating-create'),
    path('user/<int:user_id>/', RatingCreate.as_view(), name='user-ratings'),
]

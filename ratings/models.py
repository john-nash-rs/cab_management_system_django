# ratings/models.py

from django.db import models
from user.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_received')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # You can add fields to distinguish between rider and driver ratings if needed.

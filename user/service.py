from django.contrib.auth import authenticate, login
from rest_framework.exceptions import ValidationError

class UserService:
    @classmethod
    def register_rider(cls, serializer):
        if serializer.is_valid():
            rider = serializer.save()
            return rider
        else:
            raise ValidationError(serializer.errors)

    @classmethod
    def register_driver(cls, serializer):
        if serializer.is_valid():
            driver = serializer.save()
            return driver
        else:
            raise ValidationError(serializer.errors)

    @classmethod
    def sign_in(cls, request, username, password):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # You can generate and return a JWT token here for authentication
            return user
        else:
            raise ValidationError({'message': 'Invalid credentials'})

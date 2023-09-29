from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from user.serializers import RiderSerializer, DriverSerializer, UserSerializer
from .models import User, Driver, Rider
from rest_framework.decorators import api_view
from rest_framework import status

# Import your serializers and any other necessary modules

@api_view(['POST'])
@csrf_exempt
def register_rider(request):
    if request.method == 'POST':
        # Deserialize the request data using the RiderSerializer
        serializer = RiderSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new rider user
            rider = serializer.save()

            # Return a success response
            return JsonResponse({'message': 'Rider registered successfully'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def register_driver(request):
    if request.method == 'POST':
        # Deserialize the request data using the DriverSerializer
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new driver user
            driver = serializer.save()

            # Return a success response
            return JsonResponse({'message': 'Driver registered successfully'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            
            # You can generate and return a JWT token here for authentication

            return JsonResponse({'message': 'Sign-in successful'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# user/views.py
from django.forms import ValidationError
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import RiderSerializer, DriverSerializer
from .service import UserService
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def register_rider(request):
    if request.method == 'POST':
        serializer = RiderSerializer(data=request.data)
        try:
            rider = UserService.register_rider(serializer)
            return JsonResponse({'message': 'Rider registered successfully'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return JsonResponse(e.detail, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def register_driver(request):
    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        try:
            driver = UserService.register_driver(serializer)
            return JsonResponse({'message': 'Driver registered successfully'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return JsonResponse(e.detail, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = UserService.sign_in(request, username, password)
            return JsonResponse({'message': 'Sign-in successful'}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return JsonResponse(e.detail, status=status.HTTP_401_UNAUTHORIZED)

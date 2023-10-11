#!/bin/bash

# Base URL for your Django API
BASE_URL="http://localhost:8000/api"

# User Module APIs

# Rider Registration
curl --location "$BASE_URL/register/rider/" \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": {
      "username": "rider_username",
      "password": "rider_password",
      "email": "rider_email@example.com"
    }
}'

# Driver Registration
curl --location "$BASE_URL/register/driver/" \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": {
      "username": "driver_username",
      "password": "driver_password",
      "email": "driver_email@example.com"
    }
}'

# Sign in
curl --location "$BASE_URL/signin/" \
--header 'Content-Type: application/json' \
--data '{
    "username": "rider_username",
    "password": "rider_password"
}'

# Booking Module APIs

# Create Booking
curl --location "$BASE_URL/booking/" \
--header 'Content-Type: application/json' \
--data-raw '{
    "rider": 1,  # Replace with the actual rider ID
    "ride": 1,   # Replace with the actual ride ID
    "payment": 1,  # Replace with the actual payment ID
    "status": "Pending"
}'

# Cancel Booking
curl --location "$BASE_URL/booking/1/" -X DELETE

# Make Payment for Booking
curl --location "$BASE_URL/booking/1/make-payment/" \
--header 'Content-Type: application/json' \
--data-raw '{
    "ride": 1,  # Replace with the actual ride ID
    "amount": 50.00
}'

# cab_management_system_django

## Rider Registration API

curl --location 'http://localhost:8000/api/register/rider/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": {
      "username": "rider_username",
      "password": "rider_password",
      "email": "rider_email@example.com"
    }
  }'

## Driver Registration API

curl --location 'http://localhost:8000/api/register/driver/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": {
      "username": "driver_username",
      "password": "driver_password",
      "email": "driver_email@example.com"
    }
  }'

## Sign in API

curl --location 'http://localhost:8000/api/signin/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "rider_username",
    "password": "rider_password"
  }'

## Create a booking

curl --location 'http://localhost:8000/api/booking/book/' \
--header 'Content-Type: application/json' \
--data '{
    "rider": 1, 
    "status": "Pending"
}'

## Create a ride

curl --location 'http://localhost:8000/api/booking/ride/' \
--header 'Content-Type: application/json' \
--data '{
    "rider": 1, 
    "driver": 1, 
    "booking": 1, 
    "pickup_location": "Location A",
    "dropoff_location": "Location B",
    "status": "Pending"
}'

## create a payment

curl --location 'http://localhost:8000/api/booking/payment/1/' \
--header 'Content-Type: application/json' \
--data '{
    "amount" : 34,
    "status" : "Paid",
    "ride" : 1,
    "booking" : 1
}'

## Rate a user

curl --location 'http://localhost:8000/api/ratings/create/' \
--header 'Content-Type: application/json' \
--data '{
    "user": 1, 
    "rating": 4.5,
    "review": "Great experience!"
}'

## Get rating for a user
curl --location 'http://localhost:8000/api/ratings/user/1'
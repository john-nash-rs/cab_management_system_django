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

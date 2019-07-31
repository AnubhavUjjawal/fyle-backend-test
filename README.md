# Fyle Backend Coding Challenge

Essentials the applications should have:

- use PostgreSQL as a backend database
- GET API to fetch a bank details, given branch IFSC code
- GET API to fetch all details of branches, given bank name and a city
- each API should support limit & offset parameters
- APIs should be authenticated using a JWT key, with validity = 5 days.

## My Solution Stack

- WebFramework: Django
- Language: python
- swagger documentation at `<host-url>/swagger/`

## Project Local Setup

- Create a `python3` virtualenv and activate it.

- From project directory with virtualenv activated, run the following command.

  ```sh
    pip install requirements.txt
  ```

- Create a `<project_dir>/fyle_backend/local_settings.py`.

  ```py
    from .settings import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'fyle_backend',
            'USER': 'anubhavujjawal'
        }
    }
  ```

- Update the database config in `<project_dir>/fyle_backend/local_settings.py`. See [this](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04).

- From project directory with virtualenv activated, run the following command.

  ```sh
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    python manage.py runserver
  ```

- A dev server will be up and running.

## User Registration and API-usage flow

- It is recommended to checkout `GET swagger/`.

- Register using `POST accounts/register/`.
  - Sample CURL:

    ```sh
    curl -X POST "http://localhost:8000/accounts/register/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: VhOpX6dw3YfUBIRj4cy0VtRUoN6ey7Rmc0Gv1kRarACxAoHjpCo4sK6hhS0LHJv5" -d "{ \"username\": \"shiva\", \"first_name\": \"string\", \"last_name\": \"string\", \"email\": \"user@example.com\", \"password\": \"HelloJSX\", \"password_confirm\": \"HelloJSX\"}"
    ```

- After you have registered successfully, you can obtain a `JWT token` using `POST /api-token-auth/`. The validity of `JWT token` is 5 days. You can also refresh the token(while the token is still active and within 30 days of issuing of first token) using `POST api-token-refresh/`.
  - Sample CURL for getting `JWT token`:

    ```sh
    curl -X POST "http://localhost:8000/api-token-auth/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: VhOpX6dw3YfUBIRj4cy0VtRUoN6ey7Rmc0Gv1kRarACxAoHjpCo4sK6hhS0LHJv5" -d "{ \"username\": \"admin\", \"password\": \"qazwsxedc\"}"
    ```

    - Sample CURL for refreshing `JWT token`:

    ```sh
    curl -X POST "http://localhost:8000/api-token-refresh/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: Dld0ldW5jenSsA8zVGg8DlRGQHUphHSKU456prAJHQKvrgYzg66caC63JMOWqjwt" -d "{ \"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY0NTY4NjU1LCJlbWFpbCI6ImFudWJoYXZ1amphd2FsQGdtYWlsLmNvbSJ9.GMbLTZYicKyyTvXAipdFRz-xhcQ65fZBdKoW_j9h1Xs\"}"
    ```

- ### Using Bank API's

  - Search is Case-Sensitive everywhere.
  - GET API to fetch a bank details, given branch IFSC code.
    - **NOTE**: Pagination is not required for this endpoint as there will always only be a single bank branch in response.
    - Send a `GET /bank/{ifsc}/`, with `ifsc` replaced by IFSC code. Include `JWT token` in the headers as `Authorization:"JWT <token>"`

    - Sample CURL for `GET /bank/{ifsc}/`:

      ```sh
      curl -X GET "http://localhost:8000/bank/ABHY0065001/" -H "accept: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY1MDAxNjg5LCJlbWFpbCI6ImFudWJoYXZ1amphd2FsQGdtYWlsLmNvbSJ9.PB9ES8ZNLm9K7qzgupwCY3m5kVW7fFUdyLrIXun3bFo" -H "X-CSRFToken: SwW2YIBihC639fHu82K0v5eX34EVb1t59fO82WfWFetG8VxutsA42mtkW9yskD7O"
      ```

  - GET API to fetch all details of branches, given bank name and a city.
    - **NOTE**: Pagination supported for this endpoint.
    - Send a `GET /bank/?bank_name=<bank-name>&city=<city-name>&limit=<limit>&offset=<offset>`.
    - Sample request. `GET /bank/?bank_name=BHARAT+COOPERATIVE+BANK+MUMBAI+LIMITED&city=MUMBAI&limit=10&offset=20`

    - Sample CURL:

      ```sh
      curl -X GET "http://localhost:8000/bank/?limit=10&offset=20&city=MUMBAI&bank=CANARA%20BANK" -H "accept: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY1MDAzOTg5LCJlbWFpbCI6ImFudWJoYXZ1amphd2FsQGdtYWlsLmNvbSJ9.hRsOMvVn3wkOLChBuzmaaGOne1n4RE1zKQO0bH7mdrU" -H "X-CSRFToken: 9l8CxhHc5agdYSWB3bmt5ZjCk77kNI5nq40IBvlQtMDQXyMBoBcxCgyZdc1RWkJ6"
      ```

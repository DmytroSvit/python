from drf_yasg import openapi


class Examples:
    LOGIN_SUCCESS = {
        "email": "john.ivan@example.com",
        "username": "anonimus",
        "token": "JWT-token "
    }

    LOGIN_FAIL = {
        "field_1 ": [
            "error_1", "error_2"
        ],
        "field_2": [
            "error_1", "error_2"
        ],
    }

    LOGOUT_SUCCESS = {
        "massage": "Token blacklisted successfully"

    }

    LOGOUT_FAIL = {
        "detail": "Authentication credentials were not provided."

    }

    REGISTER_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "email": openapi.Schema(type=openapi.TYPE_STRING,
                                    description='email',
                                    max_length=254),
            "username": openapi.Schema(type=openapi.TYPE_STRING,
                                         description='username',
                                         max_length=255),
            "password": openapi.Schema(type=openapi.TYPE_STRING,
                                       description='Password',
                                       max_length=128),
        })

    LOGIN_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "email": openapi.Schema(type=openapi.TYPE_STRING,
                                    description='email',
                                    max_length=254),
            "password": openapi.Schema(type=openapi.TYPE_STRING,
                                       description='Password',
                                       max_length=128),
        })


class Documentations:

    LOGIN = {
        "request_body": Examples.LOGIN_PARAMETER,
        "responses": {
            "200": openapi.Response(
                description="Valid data => login (generate JWT)",
                examples={
                    "application/json": Examples.LOGIN_SUCCESS
                }
            ),
            "400": openapi.Response(
                description="Invalid data => no login",
                examples={
                    "application/json": Examples.LOGIN_FAIL
                }
            ),
            "403": openapi.Response(
                description="Invalid data => no login",
                examples={
                    "application/json": Examples.LOGOUT_FAIL
                }
            ),
        }
    }

    REGISTER = {
        "request_body": Examples.REGISTER_PARAMETER,
        "responses": {
            "201": openapi.Response(
                description="Valid data, unique email => register + JWT",
                examples={
                    "application/json": Examples.LOGIN_SUCCESS
                }
            ),
            "400": openapi.Response(
                description="Invalid input parameters = no registration",
                examples={
                    "application/json": Examples.LOGIN_FAIL
                }
            ),
            "403": openapi.Response(
                description="Invalid data => no login",
                examples={
                    "application/json": Examples.LOGOUT_FAIL
                }
            ),
        }
    }

    LOGOUT = {
        "responses": {
            "200": openapi.Response(
                description="Valid token == logout",
                examples={
                    "application/json": Examples.LOGOUT_SUCCESS
                }
            ),
            "403": openapi.Response(
                description="No login == no logout",
                examples={
                    "application/json": Examples.LOGOUT_FAIL
                }
            ),
        }
    }

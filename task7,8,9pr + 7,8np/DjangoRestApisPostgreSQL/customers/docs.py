from drf_yasg import openapi



class Examples:
    Advertisement_example = {
        "website_url": "url",
        "start_date": "date",
        "end_date": "date",
        "price": "float",
        "title": "string",
        "photo_url": "url",
        "transaction_number": "string"
    }

    Advertisement_absent = {
        "status": 404,
        "message": "The Advertisement does not exist"
    }

    Advertisement_wrong = {
        "status": 400,
        "errors": {
            "field_1": "error_1",
            "field_2": "error_2"
        }
    }

    Advertisement_add = {
        "status": 201,
        "Advertisement": Advertisement_example
    }

    Advertisement_update = {
        "status": 200,
        "message": Advertisement_example
    }

    Advertisement_delete = {
        "status": 204,
        "message": "Advertisement was deleted successfully!"
    }


    Advertisement_INPUT_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "website_url": openapi.Schema(type=openapi.TYPE_STRING,
                                          max_length=200),
            "start_date": openapi.Schema(type=openapi.TYPE_STRING,
                                      format="date"),
            "end_date": openapi.Schema(type=openapi.TYPE_STRING,
                                         format="date"),
            "price": openapi.Schema(type=openapi.TYPE_NUMBER,),
            "title": openapi.Schema(type=openapi.TYPE_STRING,
                                    max_length=64),
            "photo_url": openapi.Schema(type=openapi.TYPE_STRING,
                                        max_length=200),
            "transaction_number": openapi.Schema(type=openapi.TYPE_STRING,
                                                 description="(XX-YYY-XX/YY, X - letters, Y - numbers",
                                                 max_length=15),
        })


class Documentations:
    POST = {
        "operation_description": "Insert new Advertisement into a database",
        "responses": {
            "200": openapi.Response(
                description="Valid Advertisement sent -> write to database",
                examples={
                    "application/json": Examples.Advertisement_add
                }
            ),
            "400": openapi.Response(
                description="Invalid Advertisement sent -> discard",
                examples={
                    "application/json": Examples.Advertisement_wrong
                }
            ),

            "403": openapi.Response(
                description="Invalid Advertisement sent -> discard",
                examples={
                    "application/json": {
                                            "detail": "Authentication credentials were not provided."
                    }
                }
            ),
        }
    }

    GET = {
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain Advertisement from database",
                examples={
                    "application/json": Examples.Advertisement_example
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Advertisement_absent
                }
            ),
        }
    }

    PUT = {
        "request_body": Examples.Advertisement_INPUT_PARAMETER,
        "operation_description": "Edit Advertisement record by ID in database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain Advertisement from database",
                examples={
                    "application/json": Examples.Advertisement_update
                }
            ),
            "400": openapi.Response(
                description="Invalid Advertisement sent -> discard",
                examples={
                    "application/json": Examples.Advertisement_wrong
                }
            ),
            "403": openapi.Response(
                description="Invalid Advertisement sent -> discard",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Advertisement_absent
                }
            ),
        }
    }

    DELETE = {
        "operation_description": "Delete Advertisement by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain Advertisement from database",
                examples={
                    "application/json": Examples.Advertisement_delete
                }
            ),
            "403": openapi.Response(
                description="Invalid Advertisement sent -> discard",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Advertisement_absent
                }
            ),
        }
    }
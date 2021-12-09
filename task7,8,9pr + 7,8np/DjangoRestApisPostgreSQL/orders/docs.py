from drf_yasg import openapi


class Examples:
    Order_example = {
        "start_date": "date",
        "end_date": "date",
        "price": "float",
        "title": "string"
    }

    Order_absent = {
        "status": 404,
        "message": "The Order does not exist"
    }

    Order_wrong = {
        "status": 400,
        "errors": {
            "field_1": "error_1",
            "field_2": "error_2"
        }
    }

    Order_add = {
        "status": 201,
        "Order": Order_example
    }

    Order_delete = {
        "status": 204,
        "message": "Order was deleted successfully!"
    }


    Order_INPUT_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "start_date": openapi.Schema(type=openapi.TYPE_STRING,
                                      format="date"),
            "end_date": openapi.Schema(type=openapi.TYPE_STRING,
                                         format="date"),
            "price": openapi.Schema(type=openapi.TYPE_NUMBER,),
            "title": openapi.Schema(type=openapi.TYPE_STRING,
                                    max_length=64),

        })


class Documentations:
    GET_LIST = {
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain list of all orders of current user from database",
                examples={
                    "application/json": [
                        Examples.Order_example,
                    ]
                }
            ),
        }
    }
    POST = {
        "operation_description": "Insert new Order into a database",
        "responses": {
            "200": openapi.Response(
                description="Valid Order sent -> write to database",
                examples={
                    "application/json": Examples.Order_add
                }
            ),
            "400": openapi.Response(
                description="Invalid Order sent -> discard",
                examples={
                    "application/json": Examples.Order_wrong
                }
            ),

            "403": openapi.Response(
                description="Invalid Order sent -> discard",
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
                description="Valid id -> obtain Order from database",
                examples={
                    "application/json": Examples.Order_example
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Order_absent
                }
            ),
        }
    }


    DELETE = {
        "operation_description": "Delete Order by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain Order from database",
                examples={
                    "application/json": Examples.Order_delete
                }
            ),
            "403": openapi.Response(
                description="Invalid Order sent -> discard",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Order_absent
                }
            ),
        }
    }
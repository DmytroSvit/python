from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegistrationSerializer, LogoutSerializer
from rest_framework.permissions import IsAuthenticated


class RegistrationAPIView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def post(self, request):
        auth_value = request.headers.get("Authorization")
        print(auth_value, type(auth_value))
        token = auth_value.split()[1]

        serializer = self.serializer_class(data={"expired_token": token})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Token blacklisted successfully", status=status.HTTP_200_OK)
from rest_framework import serializers
from django.contrib.auth import authenticate
import re

from .models import User, BlackListedToken



class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['email', 'username', 'password', 'token']
        #read_only_fields = ['token']



    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, data):
        if not re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}', data['password']):
            raise serializers.ValidationError("Bad password: 1 capital 1 small 1 digit please!")

        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }

class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListedToken
        fields = "__all__"
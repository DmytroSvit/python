import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser,  PermissionsMixin)
from .usermanager import UserManager
from enum import Enum
from django.db import models


class Roles(Enum):
    admin = 0
    user = 1

    @classmethod
    def items(cls):
        return [(option.value, option.name) for option in cls]


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    role = models.IntegerField(choices=Roles.items(), default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.timestamp()
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

class BlackListedToken(models.Model):
    expired_token = models.CharField(max_length=255)

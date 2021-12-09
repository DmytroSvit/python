from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_price(value):
    if value<0:
        raise ValidationError('Price can`t be less than 0')


def validate_number(value):
    if not re.fullmatch(r'^[a-zA-Z]{2}[-]{1}[0-9]{3}[-]{1}[a-zA-Z]{2}[\/][0-9]{2}$', value):
        raise ValidationError('Invalid code. Code must be in format XX-YYY-XX/YY, where X - letters, Y - numbers')


class Advertisement(models.Model):
    website_url = models.URLField(max_length=200, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    price =  models.FloatField(validators=[validate_price])
    title = models.CharField(max_length=64, blank=False)
    photo_url = models.URLField(max_length=200, blank=False)
    transaction_number = models.CharField(max_length=15, blank=False, validators=[validate_number])





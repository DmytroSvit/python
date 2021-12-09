from django.db import models
from django.core.exceptions import ValidationError


def validate_price(value):
    if value<0:
        raise ValidationError('Price can`t be less than 0')


class Advertisement_Order(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    price =  models.FloatField(validators=[validate_price])
    title = models.CharField(max_length=64, blank=False)
    owner = models.IntegerField()


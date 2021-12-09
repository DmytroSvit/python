from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    def validate(self, values):
        if values["start_date"] > values["end_date"]:
            raise serializers.ValidationError("Start date can`t be later than End date")
        else:
            return values

    class Meta:
        model = Advertisement
        fields = ('id',
                  'website_url',
                  'start_date',
                  'end_date',
                  'price',
                  'title',
                  'photo_url',
                  'transaction_number')
        read_only_fields = (id,)

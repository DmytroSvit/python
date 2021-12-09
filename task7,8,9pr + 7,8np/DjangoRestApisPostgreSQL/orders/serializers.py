from rest_framework import serializers
from .models import Advertisement_Order


class Advertisement_OrderSerializer(serializers.ModelSerializer):

    def validate(self, values):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        owner = user.pk
        obj_data = Advertisement_Order.objects.filter(owner__exact=owner)
        if obj_data.count() >= 3:
            raise serializers.ValidationError("Too much orders!")
        if values["start_date"] > values["end_date"]:
            raise serializers.ValidationError("Start date can`t be later than End date")
        else:
            return values



    class Meta:
        model = Advertisement_Order
        fields = ('id',
                  'start_date',
                  'end_date',
                  'price',
                  'title',
                  'owner')
        read_only_fields = (id, "owner",)
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status, filters

from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.decorators import api_view
from .pagination import CustomOffsetPagination


class advertisement_list(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pagination_class = CustomOffsetPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["start_date", "end_date", "id",
                     "website_url", "photo_url", "title", "price", "transaction_number"]

    # get is auto-defined here

    def post(self, request, **kwargs):
        customer_data = JSONParser().parse(request)
        customer_serializer = AdvertisementSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class advertisement_detail(APIView):

    @staticmethod
    def get_object(pk):
        try:
            customer = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return Response({'message': 'The advertisement does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return customer

    def get(self, request, pk):
        customer = self.get_object(pk)

        # 404 return
        if isinstance(customer, Response):
            return customer

        customer_serializer = AdvertisementSerializer(customer)
        return Response(customer_serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)

        # 404 return
        if isinstance(customer, Response):
            return customer

        customer_data = JSONParser().parse(request)
        customer_serializer = AdvertisementSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data)
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)

        # 404 return
        if isinstance(customer, Response):
            return customer

        customer.delete()
        return Response({'message': 'Advertisement was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status, filters

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .pagination import CustomOffsetPagination

from drf_yasg.utils import swagger_auto_schema
from .docs import Documentations


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return getattr(request.user, "role", 1) == 0


class advertisement_list(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pagination_class = CustomOffsetPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["start_date", "end_date", "id",
                     "website_url", "photo_url", "title", "price", "transaction_number"]

    permission_classes = [IsAdminOrReadOnly]

    # get is auto-defined here

    @swagger_auto_schema(**Documentations.POST)
    def post(self, request, **kwargs):
        customer_data = JSONParser().parse(request)
        customer_serializer = AdvertisementSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class advertisement_detail(APIView):

    permission_classes = [IsAdminOrReadOnly]

    @staticmethod
    def get_object(pk):
        try:
            customer = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return Response({'detail': 'The advertisement does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return customer

    @swagger_auto_schema(**Documentations.GET)
    def get(self, request, pk):
        customer = self.get_object(pk)

        # 404 return
        if isinstance(customer, Response):
            return customer

        customer_serializer = AdvertisementSerializer(customer)
        return Response(customer_serializer.data)

    @swagger_auto_schema(**Documentations.PUT)
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

    @swagger_auto_schema(**Documentations.DELETE)
    def delete(self, request, pk):
        customer = self.get_object(pk)

        # 404 return
        if isinstance(customer, Response):
            return customer

        customer.delete()
        return Response({'detail': 'Advertisement was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import status

from .models import Advertisement_Order
from .serializers import Advertisement_OrderSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .docs import Documentations
from django.utils.decorators import method_decorator


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(**Documentations.POST)
)
class Advertisement_OrderViewSet(ModelViewSet):

    model = Advertisement_Order

    queryset = Advertisement_Order.objects.all()
    serializer_class = Advertisement_OrderSerializer

    permission_classes = [IsAuthenticated, ]


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user.pk)

    @swagger_auto_schema(**Documentations.GET_LIST)
    def list(self, request, *args, **kwargs):
        data = None
        if request.user.role == 0:
            data = self.queryset.filter()
        else:
            data = self.queryset.filter(owner=request.user.pk)

        if len(data) == 0:
            return Response({"detail": "Orders for advertisement not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**Documentations.GET)
    def retrieve(self, request, *args, **kwargs):
        data = None
        if request.user.role == 0:
            data = self.queryset.filter(pk=kwargs["pk"])
        else:
            data = self.queryset.filter(owner=request.user.pk, pk=kwargs["pk"])

        if len(data) == 0:
            return Response({"detail": "Orders for advertisement not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**Documentations.DELETE)
    def destroy(self, request, *args, **kwargs):
        data = None
        if request.user.role == 0:
            data = self.queryset.filter(pk=kwargs["pk"])
        else:
            data = self.queryset.filter(owner=request.user.pk, pk=kwargs["pk"])

        if len(data) == 0:
            return Response({"detail": "Orders for advertisement not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            data.delete()
            serializer = self.serializer_class(data, many=True)
            return Response({'detail': 'Order was deleted successfully!'}, status=status.HTTP_200_OK)






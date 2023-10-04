from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer, OrderDetailDeserializer

from products.models import Product
from products.serializers import ProductSerializer

from buyers.models import Buyer
from buyers.serializers import BuyerSerializer


# Create your views here.
class OrderListApiView(APIView):

    def get(self, request, *args, **kwargs):

        serializer = OrderDetailDeserializer(data=Order.objects.filter(), many=True)
        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'quantity': request.data.get('quantity'),
            'product': request.data.get('product_id'),
            'buyer': request.data.get('buyer_id')
        }

        serializer = OrderSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

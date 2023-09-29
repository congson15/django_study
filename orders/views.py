from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer

from products.models import Product
from products.serializers import ProductSerializer

from buyers.models import Buyer
from buyers.serializers import BuyerSerializer


# Create your views here.
class OrderListApiView(APIView):

    def get(self, request, *args, **kwargs):
        response_data = []


        for order in Order.objects.filter():
            order_dict = {
                'id': order.id,
                'buyer': {
                    'id': order.buyer.id,
                    'name': order.buyer.name,

                },
                'product': {
                    'id': order.product.id,
                    'name': order.product.name,
                    'price': order.product.price,
                    'quantity': order.quantity
                },
                'order_date': order.order_date
            }

            response_data.append(order_dict)

        return Response(response_data, status=status.HTTP_200_OK)

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

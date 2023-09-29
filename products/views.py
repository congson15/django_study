from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductListApiView(APIView):

    def get(self, request, *args, **kwargs):
        response_data = []
        for product in Product.objects.filter(deleted=False):
            product_dict = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
            }

            response_data.append(product_dict)

        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
        }
        serializer = ProductSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailApiView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)

        if not product_instance:
            return Response(
                {"message": "Not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        product_dict = {
            'id': product_instance.id,
            'name': product_instance.name,
            'price': product_instance.price,
        }
        return Response(product_dict, status=status.HTTP_200_OK)

    def put(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)

        if not product_instance:
            return Response(
                {"message": "Not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(instance=product_instance, data=request.data, partial= True)

        if not serializer.is_valid():
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


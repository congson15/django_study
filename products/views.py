from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer, ProductDetailDeserializer
from .services import get_product, get_products, create_product, update_product


# Create your views here.
class ProductListApiView(APIView):

    def get(self, request, *args, **kwargs):

        products = get_products(request)

        return Response(products, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        result, errors = create_product(request)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class ProductDetailApiView(APIView):

    def handle_get(self, product_id):

        product_instance = get_product(product_id)

        if not product_instance:
            return Response(
                {"message": "Not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return product_instance

    def get(self, request, product_id, *args, **kwargs):

        product_instance = self.handle_get(product_id)

        if isinstance(product_instance, Response):
            return product_instance

        serializer = ProductDetailDeserializer(product_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, product_id, *args, **kwargs):

        product_instance = self.handle_get(product_id)

        if isinstance(product_instance, Response):
            return product_instance

        data = request.data

        result, errors = update_product(product_instance, data)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, product_id, *args, **kwargs):

        product_instance = self.handle_get(product_id)

        if isinstance(product_instance, Response):
            return product_instance

        data = request.data

        result, errors = update_product(product_instance, data)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)

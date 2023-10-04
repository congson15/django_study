from rest_framework import serializers

from buyers.serializers import BuyerSerializer
from products.serializers import ProductSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "buyer", "product", "quantity", "order_date"]


class OrderDetailDeserializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id','buyer', 'product', 'quantity']

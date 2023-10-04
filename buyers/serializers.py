from rest_framework import serializers
from .models import Buyer

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ["id", "name", "age"]

class BuyerDetailDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ["id", "name", "age"]

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Buyer
from .serializers import BuyerSerializer


# Create your views here.
class BuyerListApiView(APIView):

    def get(self, request, *args, **kwargs):
        response_data = []
        for buyer in Buyer.objects.filter(deleted=False):
            buyer_dict = {
                'id': buyer.id,
                'name': buyer.name,
                'age': buyer.age,
            }

            response_data.append(buyer_dict)

        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
        }
        serializer = BuyerSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BuyerDetailApiView(APIView):
    def get_object(self, buyer_id):
        try:
            return Buyer.objects.get(id=buyer_id)
        except Buyer.DoesNotExist:
            return None

    def get(self, request, buyer_id, *args, **kwargs):
        buyer_instance = self.get_object(buyer_id)

        if not buyer_instance:
            return Response(
                {"message": "Not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        buyer_dict = {
            'id': buyer_instance.id,
            'name': buyer_instance.name,
            'age': buyer_instance.age,
        }
        return Response(buyer_dict, status=status.HTTP_200_OK)

    def put(self, request, buyer_id, *args, **kwargs):
        buyer_instance = self.get_object(buyer_id)

        if not buyer_instance:
            return Response(
                {"message": "Not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BuyerSerializer(instance=buyer_instance, data=request.data, partial= True)

        if not serializer.is_valid():
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, product_id, *args, **kwargs):
        buyer_instance = self.get_object(product_id)

        if not buyer_instance:
            return Response(
                {"message": "Not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        buyer_instance.deleted = True
        serializer = BuyerSerializer(instance=buyer_instance)

        if not serializer.is_valid():
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

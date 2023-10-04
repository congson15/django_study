from common.utils import validate_query_params
from .serializers import ProductSerializer
from .db import get_one, get_all


def get_product(product_id):
    query = {
        "id": product_id
    }
    return get_one(query)


def get_products(request):
    param_names = ['name', 'price', 'deleted']
    valid_params, invalid_params = validate_query_params(request, param_names)

    serializer = ProductSerializer(data=get_all(valid_params), many=True)

    serializer.is_valid()
    return serializer.data


def update_product(product, data):
    serializer = ProductSerializer(instance=product, data=data, partial=True)

    if not serializer.is_valid():
        return None, serializer.errors

    serializer.save()
    return serializer.data, None

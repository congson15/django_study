from common.utils import validate_query_params
from .serializers import ProductSerializer
from .db_manager import get_one, get_all


def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if not serializer.is_valid():
        return None, serializer.errors

    serializer.save()

    return serializer.data, None


def get_product(product_id):
    query = {
        "id": product_id
    }

    return get_one(query)


def get_products(request):
    param_names = ['name', 'price', 'deleted']

    valid_params, _ = validate_query_params(request, param_names)

    products = get_all(valid_params)

    serializer = ProductSerializer(data=products, many=True)

    serializer.is_valid()

    return serializer.data


def update_product(product, data):

    product.deleted = True

    serializer = ProductSerializer(instance=product, data=data, partial=True)

    if not serializer.is_valid():
        return None, serializer.errors

    serializer.save()

    return serializer.data, None

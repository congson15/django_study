from .models import Product


def get_one(product_id_dict):
    try:
        return get_all(product_id_dict).first()
    except Product.DoesNotExist:
        return None


def get_all(query_params = None):
    products = Product.objects.all()
    if query_params:
        return products.filter(**query_params)
    return products.filter(deleted=False)

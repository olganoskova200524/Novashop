from .models import Product


def get_products_by_category(category_id: int):
    return (
        Product.objects
        .filter(category_id=category_id)
        .select_related('category')
    )

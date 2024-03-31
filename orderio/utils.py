def get_product_order_slug(instance):
    return f"{instance.price}-{instance.user.id}"


def get_product_order_item_slug(instance):
    return f"{instance.product.title[:10]}-{instance.product.user.id}"

def get_product_image_path(instance, filename):
    return f"media/products/{instance.id}-{instance.slug}/{filename}"


def get_category_slug(instance):
    return f"{instance.title}-{instance.id}"


def get_product_slug(instance):
    return f"{instance.title}-{instance.user.id}"


def get_product_cart_slug(instance):
    return f"{instance.user.get_name()}-{instance.user.id}"


def get_product_cart_item_slug(instance):
    return f"{instance.cart.slug}-{instance.cart.id}"

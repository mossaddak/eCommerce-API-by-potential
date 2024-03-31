from django.db.models import Sum, F

from autoslug import AutoSlugField

from versatileimagefield.fields import VersatileImageField

from django.db import models

from common.models import BaseModelWithUID

from orderio.models import Order

from .choices import ProductStatus
from .utils import (
    get_product_image_path,
    get_category_slug,
    get_product_slug,
    get_product_cart_slug,
    get_product_cart_item_slug,
)
from .managers import ProductQuerySet


class Category(BaseModelWithUID):
    slug = AutoSlugField(populate_from=get_category_slug, unique=True, db_index=True)
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}"


class Product(BaseModelWithUID):
    user = models.ForeignKey("accountio.User", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from=get_product_slug, unique=True, db_index=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, choices=ProductStatus, default=ProductStatus.PUBLISHED
    )
    image = VersatileImageField(upload_to=get_product_image_path, null=True, blank=True)
    sell_count = models.PositiveIntegerField(null=True, blank=True)
    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Price: {self.price}"


class Cart(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_product_cart_slug, unique=True, db_index=True
    )
    user = models.ForeignKey("accountio.User", on_delete=models.CASCADE)

    class Meta:
        ordering = ("created_at",)
        unique_together = ("user",)

    def __str__(self):
        return f"ID: {self.id}, User: {self.user.id}"

    def get_cart_price(self):
        return (
            self.cartitem_set.aggregate(
                total_price=Sum(F("product__price") * F("quantity"))
            )["total_price"]
            or 0
        )

    def get_cart_items(self):
        return self.cartitem_set.all().select_related("product")


class CartItem(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_product_cart_item_slug, unique=True, db_index=True
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"ID: {self.id}, Cart: {self.cart.id}, Product: {self.product.id}, Quantity: {self.quantity}"

    def get_total_price(self):
        return self.product.price * self.quantity

from autoslug import AutoSlugField

from django.db.models import Sum
from django.db import models

from common.models import BaseModelWithUID

from .choices import ProductOrderStatus, ProductOrderKind
from .utils import get_product_order_slug, get_product_order_item_slug


class Order(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_product_order_slug, unique=True, db_index=True
    )
    user = models.ForeignKey("accountio.User", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=ProductOrderStatus, default=ProductOrderStatus.PLACED
    )
    address = models.ForeignKey(
        "accountio.UserAddress", on_delete=models.SET_NULL, null=True
    )
    kind = models.CharField(max_length=20, choices=ProductOrderKind)
    date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField("productio.Product", through="OrderItem")

    def __str__(self):
        return f"ID: {self.id}, Total Amount: {self.price}, Status: {self.status}"

    def get_total_item_count(self):
        return (
            self.order_items.aggregate(total_quantity=Sum("quantity"))["total_quantity"]
            or 0
        )


class OrderItem(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_product_order_item_slug, unique=True, db_index=True
    )
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey("productio.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.quantity = self.order.aggregate(total_quantity=Sum("quantity"))[
            "total_quantity"
        ]
        self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product: {self.product.title}, Quantity: {self.quantity}"

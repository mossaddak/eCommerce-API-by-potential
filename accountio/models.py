from django.db.models import Sum

from autoslug import AutoSlugField

from phonenumber_field.modelfields import PhoneNumberField

from versatileimagefield.fields import VersatileImageField

from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import BaseModelWithUID
from common.lists import COUNTRIES

from orderio.models import OrderItem
from orderio.choices import ProductOrderStatus

from productio.choices import ProductStatus

from .choices import UserKind, UserStatus, UserGender
from .utils import get_user_slug, get_user_media_path_prefix, get_user_address_slug
from .managers import CustomUserManager


class User(AbstractUser, BaseModelWithUID):
    slug = AutoSlugField(populate_from=get_user_slug, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    avatar = VersatileImageField(
        "Avatar",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(
        max_length=2, choices=COUNTRIES, default="se", db_index=True
    )
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    kind = models.CharField(
        max_length=20, choices=UserKind, default=UserKind.BUYER, db_index=True
    )
    status = models.CharField(
        max_length=20,
        choices=UserStatus,
        db_index=True,
        default=UserStatus.ACTIVE,
    )
    gender = models.CharField(
        max_length=20, blank=True, null=True, choices=UserGender, db_index=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self):
        return f"ID: {self.id}, Email: {self.email}"

    def get_name(self):
        name = " ".join([self.first_name, self.last_name])
        return name.strip()

    def get_address(self):
        return self.useraddress_set.filter(is_default=True).first()

    def get_total_cart_price(self):
        total_price = self.cart__cartitem_set.filter(
            product__status=ProductStatus.PUBLISHED
        ).aggregate(total=Sum("product__price"))
        return total_price["total"] or 0

    def get_sell_product_items(self, date=None):
        order_items = OrderItem.objects.filter(
            product__user=self, order__status=ProductOrderStatus.DELIVERED
        )
        if date:
            order_items = OrderItem.objects.filter(
                product__user=self,
                order__status=ProductOrderStatus.DELIVERED,
                order__date=date,
            )
        return order_items

    def get_total_sell_amount(self, date=None):
        total_sell_amount = OrderItem.objects.filter(
            product__user=self, order__status=ProductOrderStatus.DELIVERED
        ).aggregate(total_price=Sum("price"))["total_price"]
        if date:
            total_sell_amount = OrderItem.objects.filter(
                product__user=self,
                order__status=ProductOrderStatus.DELIVERED,
                order__date=date,
            ).aggregate(total_price=Sum("price"))["total_price"]
        return total_sell_amount or 0


class UserAddress(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_user_address_slug, unique=True, db_index=True
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    country = models.CharField(
        max_length=2, choices=COUNTRIES, default="se", db_index=True
    )
    district = models.CharField(max_length=10)
    upzilla = models.CharField(max_length=20)
    full_address = models.TextField()
    is_default = models.BooleanField(default=True)

    def __str__(self):
        return f"ID: {self.id}, Country: {self.country}, User: {self.user.get_name()}"

    def save(self, *args, **kwargs):
        existing_address = UserAddress.objects.filter(user=self.user).exclude(
            id=self.id
        )
        if existing_address:
            existing_address.update(is_default=False)
        super().save(*args, **kwargs)

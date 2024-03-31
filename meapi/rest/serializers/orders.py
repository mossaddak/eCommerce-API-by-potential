from rest_framework import serializers

from django.db import transaction

from productio.models import Cart, CartItem

from orderio.models import Order, OrderItem
from orderio.rest.serializers.orders import OrderItemSerializer

from .address import PrivateMeAddressSerializer


class PrivateMeOrderSerializer(serializers.ModelSerializer):
    address = PrivateMeAddressSerializer(read_only=True)
    quantity = serializers.IntegerField(source="get_total_item_count", read_only=True)
    items = OrderItemSerializer(read_only=True, source="order_items.all", many=True)

    class Meta:
        model = Order
        fields = [
            "uid",
            "slug",
            "price",
            "quantity",
            "items",
            "status",
            "kind",
            "address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "quantity",
            "price",
            "items",
            "status",
            "address",
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        user = self.context["request"].user

        # Getting the user cart
        cart = Cart.objects.filter(user=user).prefetch_related("cartitem_set").first()

        # Getting all cart item the request user have
        cart_items = cart.get_cart_items()

        # Getting user defult addres that must be needed
        user_address = user.get_address()

        if not cart_items:
            raise serializers.ValidationError({"detail": "Cart must not be empty."})
        if not user_address:
            raise serializers.ValidationError(
                {"detail": "Defult address must be present."}
            )

        # Set value in validate_data
        data["user"] = user
        data["cart"] = cart
        data["cart_items"] = cart_items
        data["address"] = user_address

        return data

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data["user"]
        cart = validated_data.pop("cart")
        cart_items = validated_data.pop("cart_items")

        # Creating order
        order = Order.objects.create(
            user=user,
            price=cart.get_cart_price(),
            address=validated_data.pop("address"),
            kind=validated_data["kind"],
        )

        # Creating order items
        order_items = [
            OrderItem(
                order=order,
                product=cart_item.product,
                price=cart_item.get_total_price(),
                quantity=cart_item.quantity,
            )
            for cart_item in cart_items
        ]
        OrderItem.objects.bulk_create(order_items)

        # After placing an order, the cart will be empty
        CartItem.objects.filter(cart=cart).delete()

        return validated_data

    @transaction.atomic
    def update(self, instance, validated_data):
        category = validated_data.pop("category_slug", None)
        instance.category = category
        instance.save()
        return super().update(instance, validated_data)

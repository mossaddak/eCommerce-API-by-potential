from rest_framework import serializers

from django.db import transaction

from productio.rest.serializers.products import ProductSerializer
from productio.models import Product, Cart, CartItem


class PrivateMeProductCartItemListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_slug = serializers.SlugRelatedField(
        queryset=Product.objects.filter(), slug_field="slug", write_only=True
    )
    total_price = serializers.CharField(source="get_total_price", read_only=True)

    class Meta(ProductSerializer.Meta):
        model = CartItem
        fields = [
            "uid",
            "product_slug",
            "product",
            "quantity",
            "total_price",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["uid", "total_price", "created_at", "updated_at"]

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user
        product_slug = validated_data.pop("product_slug", None)

        # Cart
        cart, _ = Cart.objects.get_or_create(user=user)

        # Cart item
        cart_item, cart_item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product_slug,
            defaults={"quantity": validated_data.get("quantity")},
        )

        # Updating cart item
        if not cart_item_created:
            cart_item.quantity += validated_data.get("quantity")
            cart_item.save()

        return validated_data


class PrivateMeProductCartItemDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = [
            "uid",
            "product",
            "quantity",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["uid", "created_at", "updated_at"]

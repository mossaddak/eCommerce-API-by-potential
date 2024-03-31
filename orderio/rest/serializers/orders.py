from rest_framework import serializers

from productio.rest.serializers.products import ProductSerializer

from ...models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "uid",
            "product",
            "quantity",
            "price",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields

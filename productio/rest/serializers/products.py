from rest_framework import serializers

from ...models import Product

from .categories import CatrgorySerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "slug",
            "title",
            "description",
            "price",
            "category",
            "status",
            "image",
        ]
        read_only_fields = ["slug"]

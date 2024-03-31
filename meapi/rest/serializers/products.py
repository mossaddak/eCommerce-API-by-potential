from rest_framework import serializers

from productio.models import Category, Product
from productio.rest.serializers.products import ProductSerializer
from productio.rest.serializers.categories import CatrgorySerializer


class PrivateMeProductSerializer(serializers.ModelSerializer):
    category = CatrgorySerializer(read_only=True)
    category_slug = serializers.SlugRelatedField(
        queryset=Category.objects.filter(), slug_field="slug", write_only=True
    )

    class Meta:
        model = Product
        fields = (
            ["uid"]
            + ProductSerializer.Meta.fields
            + ["category_slug", "created_at", "updated_at"]
        )
        read_only_fields = ["uid", "created_at", "updated_at"]

    def create(self, validated_data):
        category = validated_data.pop("category_slug", None)
        Product.objects.create(
            **validated_data, category=category, user=self.context["request"].user
        )
        return validated_data

    def update(self, instance, validated_data):
        category = validated_data.pop("category_slug", None)
        instance.category = category
        instance.save()
        return super().update(instance, validated_data)

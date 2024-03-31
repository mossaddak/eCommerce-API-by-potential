from rest_framework import serializers

from ...models import Category


class CatrgorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["slug", "title", "description"]
        read_only_fields = ["slug"]

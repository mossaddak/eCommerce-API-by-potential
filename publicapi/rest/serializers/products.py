from rest_framework import serializers

from accountio.rest.serializers.users import UserSlimSerializer

from productio.rest.serializers.products import ProductSerializer


class PublicProductSerializer(serializers.ModelSerializer):
    user = UserSlimSerializer()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ["user", "created_at", "updated_at"]
        read_only_fields = fields

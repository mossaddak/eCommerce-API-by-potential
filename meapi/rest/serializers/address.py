from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accountio.models import User, UserAddress


class PrivateMeAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = [
            "uid",
            "slug",
            "country",
            "district",
            "upzilla",
            "full_address",
            "is_default",
        ]
        read_only_fields = ("uid", "slug")

    def validate(self, data):
        if (
            data["is_default"] == False
            and not UserAddress.objects.filter(
                user=self.context["request"].user, is_default=True
            )
            .exclude(id=self.instance.id)
            .exists()
        ):
            raise ValidationError("At least one address is needed as default.")
        return super().validate(data)

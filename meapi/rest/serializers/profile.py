from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from accountio.models import User


class PrivateMeProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "uid",
            "slug",
            "first_name",
            "last_name",
            "username",
            "email",
            "avatar",
            "city",
            "country",
            "phone",
            "kind",
            "gender",
            "password",
        ]
        read_only_fields = ("uid", "slug")

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)

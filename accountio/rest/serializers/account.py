from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from ...models import User

from ...utils import get_token


class AccountRegisterSerializer(serializers.ModelSerializer):
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
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data, *args, **kwargs):
        user = super().create(validated_data, *args, **kwargs)
        user.set_password(validated_data["password"])
        user.save()
        return validated_data


class PrivateUserAccountLoginSerializer(serializers.Serializer):
    email = serializers.SlugRelatedField(
        queryset=User.objects.filter(), slug_field="email", write_only=True
    )
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_data):
        user = validated_data.get("email")
        password = validated_data.get("password")

        # Check password
        if not user.check_password(password):
            raise AuthenticationFailed()

        # Get the tokens
        (
            validated_data["refresh"],
            validated_data["access"],
        ) = get_token(user)

        return validated_data

from rest_framework import serializers

from accountio.models import User


class UserSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "slug",
            "first_name",
            "last_name",
            "avatar",
            "city",
            "country",
            "kind",
            "gender",
        ]

        read_only_fields = fields

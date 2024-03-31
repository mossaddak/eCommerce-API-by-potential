from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ...models import User

from ..serializers.account import (
    AccountRegisterSerializer,
    PrivateUserAccountLoginSerializer,
)


class AccountRegister(CreateAPIView):
    serializer_class = AccountRegisterSerializer
    permission_classes = [AllowAny]


class PrivateUserAccountLogin(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PrivateUserAccountLoginSerializer

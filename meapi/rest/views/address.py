from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)

from accountio.models import UserAddress

from ..serializers.address import PrivateMeAddressSerializer


class PrivateMeAddressList(ListCreateAPIView):
    serializer_class = PrivateMeAddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class PrivateMeAddressDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMeAddressSerializer

    def get_object(self):
        return get_object_or_404(
            UserAddress, user=self.request.user, uid=self.kwargs.get("uid", None)
        )

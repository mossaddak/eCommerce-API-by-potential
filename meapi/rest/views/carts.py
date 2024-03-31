from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)

from productio.models import CartItem

from ..serializers.carts import (
    PrivateMeProductCartItemListSerializer,
    PrivateMeProductCartItemDetailSerializer,
)

from common.permissions import IsBuyer


class PrivateMeProductCartItemList(ListCreateAPIView):
    serializer_class = PrivateMeProductCartItemListSerializer
    permission_classes = [IsBuyer]
    queryset = CartItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)


class PrivateMeProductCartItemDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMeProductCartItemDetailSerializer
    permission_classes = [IsBuyer]

    def get_object(self):
        return get_object_or_404(
            CartItem, cart__user=self.request.user, uid=self.kwargs.get("uid", None)
        )

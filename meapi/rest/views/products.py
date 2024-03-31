from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)

from productio.models import Product
from productio.choices import ProductStatus

from common.permissions import IsSeller

from ..serializers.products import PrivateMeProductSerializer


class PrivateMeProductList(ListCreateAPIView):
    permission_classes = [IsSeller]
    serializer_class = PrivateMeProductSerializer
    queryset = Product.objects.get_status_fair()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class PrivateMeProductDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSeller]
    serializer_class = PrivateMeProductSerializer
    queryset = Product.objects.get_status_fair()

    def get_object(self):
        return get_object_or_404(
            self.queryset, user=self.request.user, uid=self.kwargs.get("uid", None)
        )

    def perform_destroy(self, instance):
        instance.status = ProductStatus.REMOVED
        instance.save()

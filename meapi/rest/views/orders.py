from rest_framework import filters
from rest_framework.generics import ListCreateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from orderio.models import Order

from common.permissions import IsBuyer

from ..serializers.orders import PrivateMeOrderSerializer


class PrivateMeOrderList(ListCreateAPIView):
    permission_classes = [IsBuyer]
    serializer_class = PrivateMeOrderSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = ["created_at"]
    filterset_fields = ["status", "kind"]

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .select_related("address")
            .prefetch_related("order_items")
        )

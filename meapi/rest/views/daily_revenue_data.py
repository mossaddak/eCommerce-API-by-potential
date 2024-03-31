from rest_framework import filters
from rest_framework.generics import ListCreateAPIView

from ..serializers.daily_revenue_data import PrvateMeDailyRevenueDataSerializer

from revenueio.models import DailyRevenueData


class PrivateMeDailyRevenueDataList(ListCreateAPIView):
    serializer_class = PrvateMeDailyRevenueDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["date"]

    def get_queryset(self):
        user = self.request.user
        queryset = DailyRevenueData.objects.filter(user=user).select_related("user")
        return queryset

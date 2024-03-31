from django.urls import path

from ..views.daily_revenue_data import PrivateMeDailyRevenueDataList


urlpatterns = [
    path(
        r"",
        PrivateMeDailyRevenueDataList.as_view(),
        name="meapi.private-me-daily-revenue-data-list",
    ),
]

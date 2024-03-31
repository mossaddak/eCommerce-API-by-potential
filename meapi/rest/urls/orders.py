from django.urls import path

from ..views.orders import PrivateMeOrderList


urlpatterns = [
    path(
        r"",
        PrivateMeOrderList.as_view(),
        name="meapi.private-me-order-list",
    ),
]

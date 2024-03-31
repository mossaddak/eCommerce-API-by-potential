from django.urls import path

from ..views.address import PrivateMeAddressList, PrivateMeAddressDetails

urlpatterns = [
    path(
        r"",
        PrivateMeAddressList.as_view(),
        name="meapi.me-user-address-list",
    ),
    path(
        r"/<uuid:uid>",
        PrivateMeAddressDetails.as_view(),
        name="meapi.me-user-address-details",
    ),
]

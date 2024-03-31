from django.urls import path

from ..views.profile import PrivateMeProfileView
from ..views.address import PrivateMeAddressList

urlpatterns = [
    path(
        r"",
        PrivateMeProfileView.as_view(),
        name="meapi.user-account-profile",
    )
]

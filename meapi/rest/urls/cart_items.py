from django.urls import path

from ..views.carts import PrivateMeProductCartItemList, PrivateMeProductCartItemDetails


urlpatterns = [
    path(
        r"",
        PrivateMeProductCartItemList.as_view(),
        name="meapi.private-me-cart-item-list",
    ),
    path(
        r"/<uuid:uid>",
        PrivateMeProductCartItemDetails.as_view(),
        name="meapi.private-me-cart-item-list",
    ),
]

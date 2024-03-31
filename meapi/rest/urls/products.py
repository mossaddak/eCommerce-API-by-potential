from django.urls import path

from ..views.products import PrivateMeProductList, PrivateMeProductDetails

urlpatterns = [
    path(r"", PrivateMeProductList.as_view(), name="meapi.private-me-product-list"),
    path(
        r"/<uuid:uid>",
        PrivateMeProductDetails.as_view(),
        name="meapi.private-me-product-details",
    ),
]

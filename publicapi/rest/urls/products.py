from django.urls import path

from ..views.products import PublicProductList, PublicProductDetails


urlpatterns = [
    path(r"", PublicProductList.as_view(), name="publicapi.public-product-list"),
    path(
        r"/<slug:slug>",
        PublicProductDetails.as_view(),
        name="publicapi.public-product-details",
    ),
]

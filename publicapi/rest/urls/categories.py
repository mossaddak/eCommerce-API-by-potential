from django.urls import path

from ..views.categories import PublicProductCategoryList


urlpatterns = [
    path(
        r"",
        PublicProductCategoryList.as_view(),
        name="publicapi.public-product-category-list",
    )
]

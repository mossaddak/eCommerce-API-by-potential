from django.urls import path, include

from ..views.products import PublicProductList

urlpatterns = [path("", PublicProductList, name="webpublicio.product-list")]

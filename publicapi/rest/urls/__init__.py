from django.urls import path, include


urlpatterns = [
    path("/products", include("publicapi.rest.urls.products")),
    path("/categories", include("publicapi.rest.urls.categories"))
]

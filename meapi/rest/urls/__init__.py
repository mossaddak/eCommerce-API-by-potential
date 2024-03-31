from django.urls import path, include

urlpatterns = [
    path(
        "/profile",
        include("meapi.rest.urls.profile"),
    ),
    path(
        "/products",
        include("meapi.rest.urls.products"),
    ),
    path(
        "/cart-items",
        include("meapi.rest.urls.cart_items"),
    ),
    path(
        "/addreses",
        include("meapi.rest.urls.addreses"),
    ),
    path(
        "/orders",
        include("meapi.rest.urls.orders"),
    ),
    path("/daily-revenues", include("meapi.rest.urls.daily_revenue_data")),
]

from django.urls import path, include

urlpatterns = [
    path(
        "",
        include("webpublicio.web.urls.products"),
    )
]

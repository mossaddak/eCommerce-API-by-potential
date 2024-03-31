import os

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Change Admin Top Nav Header
admin.site.site_header = "e-Commerce Site"

schema_view = get_schema_view(
    openapi.Info(title="e-Commerce APIs", default_version="main"),
    public=False,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Swagger
    path(
        r"api/v1/docs",
        schema_view.with_ui("swagger", cache_timeout=10),
        name="schema-swagger-ui",
    ),
    # Django Admin Panel
    path("admin", admin.site.urls),
    # Website
    path("", include("webpublicio.web.urls")),
    # Account
    path("api/v1/account", include("accountio.rest.urls")),
    # My endpoints
    path("api/v1/me", include("meapi.rest.urls")),
    # Public endpoints
    path("api/v1/public", include("publicapi.rest.urls")),
    # Profiling
    # path("profiling", include("silk.urls", namespace="silk")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

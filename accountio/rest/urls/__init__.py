from django.urls import path, include

urlpatterns = [
    path(r"/", include("accountio.rest.urls.account")),
]

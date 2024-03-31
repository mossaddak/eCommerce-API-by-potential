from django.urls import path

from ..views.account import AccountRegister, PrivateUserAccountLogin

urlpatterns = [
    path(r"register", AccountRegister.as_view(), name="accountio.account-register"),
    path(
        r"login",
        PrivateUserAccountLogin.as_view(),
        name="accountio.user-account-login",
    ),
]

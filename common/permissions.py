from rest_framework import permissions

from accountio.choices import UserKind


class IsSeller(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user
        if user.is_active and user.kind == UserKind.SELLER:
            return True
        return False


class IsBuyer(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user
        if user.is_active and user.kind == UserKind.BUYER:
            return True
        return False

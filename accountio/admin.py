from django.contrib import admin

from .models import User, UserAddress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("uid", "first_name", "last_name", "email", "status", "kind")
    search_fields = ("uid", "id", "email", "status", "kind", "created_at")


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    model = User
    list_display = ("uid", "is_default", "country", "district", "upzilla")
    search_fields = ("uid", "country", "district", "upzilla")

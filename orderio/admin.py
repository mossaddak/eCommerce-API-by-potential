from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("uid", "status", "kind", "price", "date")
    search_fields = ("uid", "slug", "status", "kind")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ("uid", "quantity", "price", "date")
    search_fields = ("uid", "slug")

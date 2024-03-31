from django.contrib import admin

from .models import Category, Product, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("slug", "title")
    search_fields = ("uid", "id", "slug", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("slug", "title", "price", "status")
    search_fields = ("uid", "id", "slug", "title", "price", "status")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ("slug",)
    search_fields = ("uid", "id", "slug")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ("slug", "product")
    search_fields = ("uid", "id", "slug")

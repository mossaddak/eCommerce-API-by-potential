from django.contrib import admin

from .models import DailyRevenueData


@admin.register(DailyRevenueData)
class DailyRevenueDataAdmin(admin.ModelAdmin):
    model = DailyRevenueData
    list_display = ("uid", "sell_count", "sell_amount", "date")
    search_fields = ("uid", "slug", "date")

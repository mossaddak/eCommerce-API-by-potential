from django.db import models

from common.models import BaseModelWithUID


class DailyRevenueData(BaseModelWithUID):
    user = models.ForeignKey(
        "accountio.User", related_name="get_daily_revenue", on_delete=models.CASCADE
    )
    sell_count = models.PositiveIntegerField(default=0)
    sell_amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"ID: {self.id}, Sell Count: {self.sell_count}, Sell Amount: {self.sell_amount}, Date: {self.date}"

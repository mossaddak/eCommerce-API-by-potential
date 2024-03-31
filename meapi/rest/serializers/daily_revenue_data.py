from rest_framework import serializers

from django.db import transaction

from revenueio.models import DailyRevenueData

from orderio.rest.serializers.orders import OrderItemSerializer


class PrvateMeDailyRevenueDataSerializer(serializers.ModelSerializer):
    sell_items = OrderItemSerializer(
        source="user.get_sell_product_items", read_only=True, many=True
    )

    class Meta:
        model = DailyRevenueData
        fields = ["sell_count", "sell_amount", "sell_items", "date"]
        read_only_fields = ["sell_count", "sell_amount", "sell_items"]

    @transaction.atomic
    def create(self, validated_data):
        date = validated_data["date"]
        user = self.context["request"].user
        sell_amount = user.get_total_sell_amount(date)
        sell_count = user.get_sell_product_items(date).count()

        # Create revenue short list baed on the date
        daily_date_revenue = DailyRevenueData.objects.filter(
            date=date, user=user
        ).first()

        if daily_date_revenue and sell_count > 0:
            daily_date_revenue.sell_amount = sell_amount
            daily_date_revenue.sell_count = sell_count
            daily_date_revenue.save()

        elif sell_count > 0 and not daily_date_revenue:
            DailyRevenueData.objects.create(
                user=user, sell_count=sell_count, sell_amount=sell_amount, date=date
            )

        else:
            raise serializers.ValidationError(
                {"detail": "You don't have any sell for the given date."}
            )

        return validated_data

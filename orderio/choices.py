from django.db import models


class ProductOrderStatus(models.TextChoices):
    PLACED = "PLACED", "Placed"
    ON_THE_WAY = "ON_THE_WAY", "On The Way"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELED = "CANCELED", "Cancled"

class ProductOrderKind(models.TextChoices):
    COD = "COD", "Cash On Delivery"
    ONLINE = "ONLINE", "Online"

from django.db import models


class ProductStatus(models.TextChoices):
    PUBLISHED = "PUBLISHED", "Published"
    UNPUBLISHED = "UNPUBLISHED", "Un Published"
    REMOVED = "REMOVED", "Removed"

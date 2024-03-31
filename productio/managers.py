from django.db import models

from .choices import ProductStatus


class ProductQuerySet(models.QuerySet):
    def get_status_fair(self):
        return self.filter(
            status__in=[ProductStatus.PUBLISHED, ProductStatus.UNPUBLISHED]
        )

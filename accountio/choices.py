from django.db import models


class UserKind(models.TextChoices):
    SELLER = "SELLER", "Seller"
    BUYER = "BUYER", "Buyer"


class UserStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACTIVE = "ACTIVE", "Active"
    PENDING = "PENDING", "Pending"
    DISABLED = "DISABLED", "Disabled"


class UserGender(models.TextChoices):
    FEMALE = "FEMALE", "Female"
    MALE = "MALE", "Male"
    OTHER = "OTHER", "Other"

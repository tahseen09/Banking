import uuid
from django.db import models

from individual.models import Individual


class Account(models.Model):
    account_number = models.UUIDField(default=uuid.uuid4, unique=True)
    account_type = models.CharField(max_length=100, default="SAVINGS")
    account_holder = models.ForeignKey(to=Individual, on_delete=models.CASCADE)

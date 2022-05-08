from django.db import models


class Individual(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name
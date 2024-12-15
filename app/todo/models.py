from django.db import models
from django.conf import settings

import uuid

# Create your models here.


class TodoTask(models.Model):
    """
    A model of the tasks a user has to do
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "created_at"]

    def __str__(self):
        return (self.name[:50] + "...") if len(self.name) > 50 else self.name

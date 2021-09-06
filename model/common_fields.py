from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    """ Abstract base classe some common information """
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ['-created']
        abstract = True

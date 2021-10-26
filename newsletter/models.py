from django.db import models
from model.common_fields import BaseModel


class Subscriber(BaseModel):
    email = models.EmailField(unique=True, verbose_name='Email')
    confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"

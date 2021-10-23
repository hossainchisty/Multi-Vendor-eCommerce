from django.db import models


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.capitalize()}, wents to contact with you!'

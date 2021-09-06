from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField
from model.common_fields import BaseModel

from .manager import UserManager


class User(AbstractUser):
    """ Custome User model"""

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    objects = UserManager()


class Customer(BaseModel):
    """Customer model for storing customer information"""

    user = models.OneToOneField(
        User, related_name='customer', on_delete=models.CASCADE)
    full_name = models.CharField(
        max_length=255, help_text="Enter your first and last name")
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?880?\d{9,11}$', message="Phone number must be entered in the format: '+8801234233566'. Up to 11 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=255)
    country = CountryField()

    def get_user_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = f"{self.full_name}"
        return full_name.strip()

    def get_user_email(self):
        """Returns the email of the user."""
        return self.email

    class Meta:
        verbose_name_plural = "Customer"

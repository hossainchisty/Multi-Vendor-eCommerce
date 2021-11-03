from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
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
    full_name = models.CharField(max_length=255)
    image = CloudinaryField('avatar', null=True, blank=True)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?880?\d{9,11}$', message="Phone number must be entered in the format: '+8801234233566'. Up to 11 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=255)
    country = CountryField()

    def __str__(self):
        return self.full_name

    @property
    def get_user_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = f"{self.full_name}"
        return full_name.strip()

    class Meta:
        verbose_name_plural = "Customer"

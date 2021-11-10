from cloudinary.models import CloudinaryField

from customers.models import User
from django.core.validators import RegexValidator
from django.db import models
from model.common_fields import BaseModel


class Vendor(BaseModel):
    """Vendor model for storing vendor information"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    vendor_name = models.CharField(max_length=100)
    shop_logo = CloudinaryField('logo', null=True, blank=True)
    owner_name = models.CharField(max_length=100, null=True)
    nid_number = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?880?\d{9,11}$', message="Phone number must be entered in the format: '+8801234233566'. Up to 11 digits allowed.")
    mobile_number = models.CharField(
        validators=[phone_regex], max_length=17, null=True)

    email = models.EmailField()

    address = models.TextField(null=True)

    def __str__(self):
        return f'{self.vendor_name}'

    class Meta:
        verbose_name_plural = "Vendors"

from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.timezone import now
from taggit.managers import TaggableManager
from vendor.models import Vendor
from customers.models import Customer
from model.common_fields import BaseModel


class Category(models.Model):
    """ Category model """
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Product(BaseModel):
    """ Product model """
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    SIZE_CHOICE = (
        ("m", "M"),
        ("l", "L"),
        ("xl", "XL"),
    )
    size = models.CharField(
        max_length=10, choices=SIZE_CHOICE, null=True, blank=True)
    image = CloudinaryField('image')
    available = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)

    rating = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    numbersOfReview = models.IntegerField(null=True, blank=True, default=0)
    countInStock = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(Customer)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    class Meta:
        verbose_name_plural = 'Products'

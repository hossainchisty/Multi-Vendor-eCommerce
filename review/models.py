from cloudinary.models import CloudinaryField

from customers.models import Customer
from django.db import models
from django.utils.translation import gettext as _
from model.common_fields import BaseModel
from product.models import Product


class Review(BaseModel):
    """ Review model for products """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Star(models.IntegerChoices):
        VS = 5, _('Very satisfied')
        ST = 4, _('Satisfied')
        NT = 3, _('Neutral')
        US = 2, _('Unsatisfied')
        VN = 1, _('Very unsatisfied')

    star = models.PositiveSmallIntegerField(
        _("stars"), choices=Star.choices, default=5)

    reviewImage = CloudinaryField('image', null=True, blank=True)

    feedback = models.TextField(
        help_text="Please share your feedback about the product was the product as described? What is the quality like?",
    )
    riderReview = models.TextField(
        help_text="How was your overall experience with our rider?",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Customer: {self.customer} - Product: {self.product} Rating: - {self.star}"

    class Meta:
        ordering = ('-star',)
        verbose_name_plural = _("Customer feedback")

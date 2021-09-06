from cloudinary.models import CloudinaryField
from customers.models import Customer
from django.db import models
from django.utils.translation import gettext_lazy as _
from product.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    isPaid = models.BooleanField(default=False)
    paid_date = models.DateField(auto_now_add=True)

    isDelivered = models.BooleanField(default=False)
    delivered_date = models.DateField(auto_now_add=True)

    isCancelled = models.BooleanField(default=False)
    isReturn = models.BooleanField(default=False)

    order_created = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Out for delivery", "Out for delivery"),
        ("Delivered", "Delivered"),
        ('archived', _('Archived - not available anymore')),
    )
    status = models.CharField(
        max_length=200, null=True, blank=True, choices=STATUS)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product_title = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_discount_price = models.DecimalField(
        max_digits=6, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=1)
    product_image = CloudinaryField('image')

    def __str__(self):
        return self.product_title

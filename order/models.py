from customers.models import Customer
from django.db import models
from django.utils.translation import gettext_lazy as _
from product.models import Product
from vendor.models import Vendor


class Order(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.TextField(null=True, blank=True)
    zipcode = models.CharField(max_length=250, null=True)
    place = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    isPaid = models.BooleanField(default=False)
    paid_date = models.DateTimeField()

    isDelivered = models.BooleanField(default=False)
    delivered_date = models.DateTimeField()

    isCancelled = models.BooleanField(default=False)
    isReturn = models.BooleanField(default=False)

    order_created = models.DateTimeField(auto_now_add=True)
    customer = models.ManyToManyField(Customer)

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def get_total_item_price(self):
        '''
        This method is used to get the total price of the item.
        '''
        return self.quantity * self.product.price

    @property
    def get_total_item_discount(self):
        '''
        This method is used to get the total discount of the item.
        '''
        return self.quantity * self.product.discount

    @property
    def get_amount_saved(self):
        '''
        This method is used to get the amount saved of the item.
        '''
        return self.get_total_item_price() - self.get_total_item_discount()

    @property
    def get_final_price(self):
        '''
        This method is used to get the final price of the item.
        '''
        if self.product.discount:
            return self.get_total_item_discount()
        return self.get_total_item_price()

    @property
    def get_delivery_date(self):
        return self.order.delivered_date

    @property
    def get_delivery_status(self):
        return self.order.status

    def __str__(self):
        return self.product.title

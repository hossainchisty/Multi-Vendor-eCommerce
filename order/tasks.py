from celery import shared_task

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import OrderItem


@shared_task
def send_order_confirmation_mail(order_id):
    ''' Asynchronously send email after order has been complete. '''
    orders = OrderItem.objects.filter(id=order_id, order__isPaid=True)
    for order in orders:
        body = render_to_string("mail/CartEmail.html", {"order": order})
        mail = EmailMessage(
            subject="your order has been confirmed",
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[order.customer.email],
        )
        mail.content_subtype = "HTML"
        mail.send()
        return "Confirmation mail sent to {}".format(order.email)

from celery import shared_task

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Subscriber


@shared_task
def async_send_newsletter():
    '''
    Asynchronously send newsletter to all subscribers.
    Time period:
        - Time zone: Asia/Dhaka, Bangladesh.
        - Every weeks at 00:00 ⏰
    '''
    confirme_subscribers = Subscriber.objects.filter(confirmed=True)
    for subscriber in confirme_subscribers:
        body = render_to_string("newsletter/mail/newsletter.html")
        mail = EmailMessage(
            subject="Newsletter🎉",
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[subscriber.email],
        )
        mail.content_subtype = "HTML"
        mail.send()
        return "Newsletter sent to {}".format(subscriber.email)

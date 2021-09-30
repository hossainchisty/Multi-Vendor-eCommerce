from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import threading


class EmailThread(threading.Thread):
    ''' Thread to send email in background. '''

    def __init__(self, mail):
        self.mail = mail
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.mail.send()
        except Exception as e:
            print(f'{e=}')


def send_welcome_mail(request, user):
    """ Send welcome mail to customer. """
    current_site = get_current_site(request)

    body = render_to_string("customer/mail/welcome_email.html",
                            {'current_site': request.META['HTTP_USER_AGENT'], 'domain': current_site.domain, 'user': request.user.customer})

    mail = EmailMessage(
        subject="Welcome to Lomofy!",
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[request.user.customer.email],
    )
    mail.content_subtype = "HTML"
    return None

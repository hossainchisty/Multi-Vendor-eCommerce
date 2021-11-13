import threading

from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class EmailThread(threading.Thread):
    ''' Thread to send email in background. '''

    def __init__(self, mail):
        self.mail = mail
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.mail.send()
        except Exception as e:
            messages.error(request, 'Error sending email: %s' % e)


def send_welcome_mail(request, user):
    ''' Send welcome mail to vendor. '''
    current_site = get_current_site(request)

    body = render_to_string("vendor/mail/welcome_email.html",
                            {'current_site': request.META['HTTP_USER_AGENT'], 'domain': current_site.domain, 'user': request.user.vendor})

    mail = EmailMessage(
        subject="Welcome to Lomofy!",
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[request.user.vendor.email],
    )
    mail.content_subtype = "HTML"
    mail.send()
    return None

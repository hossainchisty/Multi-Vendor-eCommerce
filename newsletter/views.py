from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect

from .models import Subscriber
from .tasks import async_send_newsletter


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subscriber = Subscriber(email=email, confirmed=True)
        if subscriber == Subscriber.objects.filter(email=subscriber.email):
            messages.error(request, 'You are already subscribed to our newsletter!')
            return redirect('home')
        else:
            try:
                subscriber.save()
                async_send_newsletter.delay()
                messages.success(request, 'You have been subscribed to our newsletter!')
                return redirect('home')
            except IntegrityError as e:
                messages.error(request, 'You are already subscribed to our newsletter!')
                return redirect('home')
    else:
        return redirect('home')


def unsubscribe(request):
    confirme_subscribers = Subscriber.objects.get(email=request.GET['email'])
    for subscriber in confirme_subscribers:
        subscriber.delete()
        messages.success(request, 'You have successfully unsubscribed from our newsletter!')
        return redirect('home')

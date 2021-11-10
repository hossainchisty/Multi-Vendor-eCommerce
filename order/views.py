import stripe

from cart.cart import Cart
from customers.decorators import customer_required
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from order.models import Order, OrderItem

from .forms import CheckoutForm
from .tasks import send_order_confirmation_mail
from .utilities import order_checkout


@customer_required
@cache_page(60 * 5)
def customerReturns(request):
    ''' customer order return history.'''
    return_products = OrderItem.objects.filter(customer=request.user.customer, order__isReturn=True)
    return render(request, 'order/return.html', {'return_products': return_products})


@customer_required
@cache_page(60 * 6)
def customerCancellations(request):
    ''' customer order cancellation history.'''
    cancel_products = OrderItem.objects.filter(customer=request.user.customer, order__isCancelled=True)
    return render(request, 'order/cancellation.html', {'cancellations': cancel_products})


@customer_required
@cache_page(60 * 2)
def customerOrderHistory(request):
    ''' customer oder purchased order history. '''
    orders = Order.objects.filter(customer=request.user.customer).order_by('-id')
    order_items = OrderItem.objects.filter(order__customer=request.user.customer).order_by('-id')
    return render(request, 'order/order_history.html', {'orders': orders, 'order_items': order_items})


@customer_required
def checkout(request):
    ''' customer order checkout form payment method. '''
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']
            try:
                charge = stripe.Charge.create(amount=int(cart.get_total_price() * 100),
                                              currency='usd',
                                              description='Example charge',
                                              source=stripe_token)

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order = order_checkout(request, first_name, last_name, email,
                                       address, zipcode, place, phone, cart.get_total_price())
                order.isPaid = True

                # order confirmation email to customer
                send_order_confirmation_mail.delay(order.id)
                return redirect('order:order_complete')
            except Exception as error:
                print(f'{error=}')
                messages.error(request, 'Somethings went wrong!')
        else:
            messages.error(request, 'Invalid form!')
    else:
        form = CheckoutForm()
    return render(request, 'order/checkout.html', {'form': form, 'stripe_pub_key': settings.STRIPE_PUB_KEY, })


@customer_required
@cache_page(60 * 60)
def order_complete(request):
    ''' customer ordered complete details.'''
    for item in Cart(request):
        print(item['product'].customer)
    completed_order = Order.objects.filter(customer=request.user.customer, isPaid=True)
    order_item = OrderItem.objects.filter(customer=request.user.customer)
    return render(request, 'order/confirmation.html', {'orders': completed_order, 'order_items': order_item})


@customer_required
@cache_page(60 * 60)
def order_details(request, order_id):
    ''' customer purchased order details. '''
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order/order_details.html', {'orders': order, 'order_items': order_items})

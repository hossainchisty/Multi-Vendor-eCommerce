from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


def customer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='customer_sign_in'):
    '''Decorator for views that checks that the logged in user is a customer.'''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_customer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def vendor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''Decorator for views that checks that the logged in user is a vendor.'''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_vendor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def unauthenticated_user(view_func):
    '''Decorator for views that checks that the user is authenticated.'''
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

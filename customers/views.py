from django.contrib import messages
from django.contrib.auth import (
    authenticate, login, update_session_auth_hash, views as auth_views,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from order.models import OrderItem


from .decorators import customer_required
from .forms import CustomerSignUpForm, CustomerUpdateForm
from .utils import service


@customer_required
@login_required(login_url='customer_sign_in')
def CustomerProfile(request):
    # product = Product.objects.filter(created_by=vendor)
    order = OrderItem.objects.all()

    context = {
        'customer': request.user.customer,
        'orders': order,
        # 'products': product,
    }

    return render(request, 'customer/customer_profile.html', context)


@customer_required
@login_required(login_url='customer_sign_in')
def CustomerProfileUpdate(request):
    ''' Update customer profile '''
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('customer_profile')
    else:
        form = CustomerUpdateForm(instance=request.user.customer)
        context = {
            'form': form,
        }
        return render(request, 'customer/customer_profile_edit.html', context)


def CustomerSignUpView(request):
    ''' Sign up view for new customer account.'''
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for registering. You are now logged in.')
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)
            service.send_welcome_mail(request, request.user.customer.email)
            return redirect('/')
        else:
            messages.error(request, 'Invalid form.')
    else:
        form = CustomerSignUpForm()
        return render(request, 'customer/sign_up.html', {'form': form})


@customer_required
@login_required(login_url='customer_sign_in')
def change_password_view(request):
    '''A form for allowing customer to change with old password '''
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Change Successfully!")
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "customer/password_change.html", {"form": form})


class SignInView(auth_views.LoginView):
    ''' Sign in for customer '''
    form_class = AuthenticationForm
    template_name = 'customer/sign_in.html'

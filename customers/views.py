from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CustomerSignUpForm, CustomerUpdateForm
from .models import User


@login_required(login_url='customer_sign_in')
def CustomerProfile(request):
    context = {
        'customer': request.user.customer,
    }
    return render(request, 'customer/customer_profile.html', context)


@login_required(login_url='customer_sign_in')
def CustomerProfileUpdate(request):
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


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer/sign_up.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_vaild(self, form):
        user = form.save()
        messages.success(
            self.request, 'New customer account created successfully')
        login(self.request, user)
        return redirect('core:home')


class SignInView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'customer/sign_in.html'

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .models import User

from .forms import CustomerSignUpForm
from .models import Customer


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

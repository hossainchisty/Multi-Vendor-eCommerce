from customers.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from vendor.decorators import vendor_required
from vendor.forms import VendorSignUpForm
from vendor.models import Vendor


class VendorSignUpView(CreateView):
    ''' Sign up a new vendor '''
    model = User
    form_class = VendorSignUpForm
    template_name = 'vendor/signup.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_vaild(self, form):
        user = form.save()
        messages.success(
            self.request, 'New vendor account created successfully')
        login(self.request, user)
        return redirect('core:home')

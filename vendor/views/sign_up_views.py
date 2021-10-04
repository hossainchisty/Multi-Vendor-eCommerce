from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from vendor.forms import VendorSignUpForm
from vendor.utils import service


def VendorSignUpView(request):
    ''' Sign up a new vendor '''
    if request.method == 'POST':
        form = VendorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            '''
            auto sign in after sign up
            '''
            login(request, user)
            messages.success(request, f'Account has been successfully created as {request.user.vendor.email} ')
            service.send_welcome_mail(request, request.user.vendor.email)
            return redirect('vendor:root_path')
    else:
        form = VendorSignUpForm()
    return render(request, 'vendor/sign_up.html', {'form': form})

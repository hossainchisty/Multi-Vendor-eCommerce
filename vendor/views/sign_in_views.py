from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class SignInView(LoginView):
    ''' Sign in for vendor '''
    form_class = AuthenticationForm
    template_name = 'vendor/sign_in.html'
    redirect_field_name = 'vendor:root_path'
    success_url = 'vendor:root_path'

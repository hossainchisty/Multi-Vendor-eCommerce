from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django_countries.fields import CountryField

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm

from .models import Customer, User


class CustomerSignUpForm(UserCreationForm):
    country = CountryField(
        blank_label='(Select country)',).formfield(null=True)
    address = forms.CharField(widget=forms.Textarea)
    full_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=17)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ["password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('full_name',
                  'email', 'phone_number', 'country', 'address', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.email = self.cleaned_data.get('email')
        customer.country = self.cleaned_data.get('country')
        customer.address = self.cleaned_data.get('address')
        customer.full_name = self.cleaned_data.get('full_name')
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.save()

        return customer


class CustomerUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'email', 'image', 'phone_number', 'country', 'address')

from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=250)
    zipcode = forms.CharField(max_length=10)
    place = forms.CharField(max_length=100)
    stripe_token = forms.CharField(max_length=100)

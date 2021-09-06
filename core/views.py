from django.shortcuts import render
from product.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

from django.shortcuts import render


def cart_list(request):
    return render(request, 'cart/cart.html')

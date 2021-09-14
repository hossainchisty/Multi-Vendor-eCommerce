from django.contrib import messages
from django.shortcuts import redirect, render

from .cart import Cart


def cart_list(request):
    cart = Cart(request)

    remove_from_cart = request.GET.get('remove_from_cart')
    change_quantity = request.GET.get('change_quantity')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        messages.info(request, 'Product remove from cart!')
        return redirect('cart:cart_list')

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart:cart_list')

    return render(request, 'cart/cart.html')

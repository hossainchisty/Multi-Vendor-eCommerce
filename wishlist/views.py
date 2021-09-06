from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from product.models import Product
from django.contrib import messages


def product_wishlist(request):
    ''' Display the products in the wishlist '''
    products = Product.objects.filter(wishlist=request.user.customer)
    return render(request, 'wishlist/product_wishlist.html', {'products': products})


def add_to_wishlist(request, product_id):
    ''' if user has already added the product to the wishlist, 
        then remove it from the wishlist else create a new wishlist item '''

    product = get_object_or_404(Product, id=product_id)

    if product.wishlist.filter(id=request.user.customer.id).exists():
        product.wishlist.remove(request.user.customer)
        messages.info(request, f'{product.title} remove form wishlist!')
    else:
        product.wishlist.add(request.user.customer)
        messages.success(
            request, f'{product.title} was added to your wishlist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

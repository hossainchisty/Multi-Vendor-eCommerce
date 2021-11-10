from customers.decorators import customer_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from product.models import Product


@cache_page(60 * 5)
@customer_required
def product_wishlist(request):
    ''' Display the products in the wishlist '''
    products = Product.objects.filter(wishlist=request.user.customer)
    return render(request, 'wishlist/product_wishlist.html', {'products': products})


@customer_required
def add_to_wishlist(request, product_id):
    '''
    if user has already added the product to the wishlist, then remove it from the wishlist else create a new wishlist item.
    '''

    product = get_object_or_404(Product, id=product_id)

    if product.wishlist.filter(id=request.user.customer.id).exists():
        product.wishlist.remove(request.user.customer)
        messages.info(request, f'{product.title} remove form wishlist!')
    else:
        product.wishlist.add(request.user.customer)
        messages.success(
            request, f'{product.title} was added to your wishlist!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

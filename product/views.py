from cart.cart import Cart
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import AddToCartForm
from .models import Product


@cache_page(60 * 5)
def product_detail(request, category_slug, product_slug, product_id):
    '''	Product detail & add to cart view '''
    products = Product.objects.get(category__slug=category_slug, slug=product_slug, pk=product_id)
    '''	Recently viewed products '''
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        product = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(
            product, key=lambda x: request.session['recently_viewed'].index(x.id)
        )

        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 3:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True

    cart = Cart(request)
    products = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=products.id, quantity=quantity, update_quantity=False)
            return redirect('cart:cart_list')
    else:
        form = AddToCartForm()

    context = {
        'form': form,
        'products': products,
        'recently_viewed_products': recently_viewed_products,
    }
    return render(request, 'product/single_product.html', context)

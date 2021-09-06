from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def product_detail(request, category_slug, product_slug):
    '''	Product detail view '''
    products = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug)

    return render(request, 'product/single_product.html', {'products': products})

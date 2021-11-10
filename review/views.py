from customers.decorators import customer_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from order.models import OrderItem
from review.models import Review

from .forms import ReviewForm


@cache_page(60 * 60)
@customer_required
def customerReviewHistory(request):
    ''' customer purchased product review history.'''
    reviews = Review.objects.filter(customer=request.user.customer, product__is_review=True)
    return render(request, 'review/review.html', {'reviews': reviews})


@cache_page(60 * 60)
@customer_required
def toBeReviewed(request):
    ''' customer who hasn't Reviewed product.'''
    # Get all the products that are not review
    unreview_product = Review.objects.filter(customer=request.user.customer, product__is_review=False)
    return render(request, 'review/unreview.html', {'unreview_product': unreview_product})


@customer_required
def writeReview(request):
    ''' customer purchased product review. '''
    product = OrderItem.objects.filter(order__customer=request.user.customer)
    for item in product:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = item.product
                review.customer = request.user.customer
                review.feedback = request.POST.get('product_review_text')
                review.riderReview = request.POST.get('rider_rate_text')
                review.product.is_review = True
                review.save()
                return redirect('customer_product_review')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = ReviewForm()
        return render(request, 'review/write_review.html', {'form': form, 'product': product})

from django.urls import path

from . import views

urlpatterns = [
    path('', views.customerReviewHistory, name='customer_review_history'),
    path('pending/', views.toBeReviewed, name='customer_to_be_reviewed'),
    path('write-review/', views.writeReview, name='customer_product_review'),
]

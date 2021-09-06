from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_wishlist, name='product_wishlist'),
    path('<int:product_id>', views.add_to_wishlist, name='add_to_wishlist'),
]

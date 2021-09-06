from django.urls import path
from .views import product_detail

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/',
         product_detail, name='product_detail'),
    
]

from django.urls import path

from .views import product_detail

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/<int:product_id>/', product_detail, name='product_detail'),

]

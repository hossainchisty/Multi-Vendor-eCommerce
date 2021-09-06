from django.urls import path
from vendor.views import vendor_signup_view as vendor_views
from vendor.views import add_product_view as product_views


urlpatterns = [
    path('new', vendor_views.VendorSignUpView.as_view(), name='vendor_signup'),


    path('add-product', product_views.add_product_view, name='add_product'),

]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog', include('blog.urls')),
    path('vendor/', include('vendor.urls')),
    path('customer/', include('customers.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('wishlist/', include('wishlist.urls')),
]

import debug_toolbar

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('vendor/', include('vendor.urls')),
    path('customer/', include('customers.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('order/', include('order.urls')),
    path('review/', include('review.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

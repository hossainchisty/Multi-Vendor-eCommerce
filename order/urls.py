from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('confirmation', views.order_complete, name='order_complete'),
    path('returns', views.customerReturns, name='customer_returns'),
    path('cancellation', views.customerCancellations, name='customer_cancellation'),
    path('history', views.customerOrderHistory, name='customer_order_history'),
    path('view/<int:order_id>', views.order_details, name='order_details'),
]

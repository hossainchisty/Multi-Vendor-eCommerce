from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('new', views.CustomerSignUpView.as_view(), name='customer_sign_up'),
    path('sign-in', views.SignInView.as_view(), name='customer_sign_in'),
    path(
        "sign-out/",
        auth_views.LogoutView.as_view(template_name="customer/logout.html"),
        name="customer_sign_out",
    ),

]

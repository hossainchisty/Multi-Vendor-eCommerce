from django.urls import reverse
from django.test import TestCase, override_settings
from customers import views
# from django.contrib.auth import views as auth_views


class TestCustomerUrl(TestCase):
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_anonymous_cannot_see_profile_url(self):
        response = self.client.get(reverse('customer_profile'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/customer/profile/')

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    # def test_anonymous_cannot_see_change_password_page(self):
    #     response = self.client.get(reverse('change_password'))
    #     self.assertRedirects(response, reverse('customer_sign_in') + '?next=/customer/change/password/')

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_anonymous_cannot_see_profile_update_url(self):
        response = self.client.get(reverse('customer_profile_update'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/customer/profile/update/')

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_sign_in_url(self):
        ''' test that sign in url '''
        response = self.client.get(reverse('customer_sign_in'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, views.SignInView.as_view().__name__)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_sign_up_url(self):
        ''' test sign up url '''
        response = self.client.get(reverse('customer_sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, views.CustomerSignUpView.__name__)

    # @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    # def test_customer_sign_out_view(self):
    #     ''' test the sign out view '''
    #     response = self.client.get(reverse('customer_sign_out'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.resolver_match.func.__name__, auth_views.LogoutView.as_view().__name__)

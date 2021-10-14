from django.urls import reverse
from django.test import TestCase, override_settings


class TestOrderUrls(TestCase):
    '''
    Test suite for review modules.
    '''
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_order_history(self):
        '''
        Test that the url for the customer order history is correct.
        '''
        url = reverse('order:customer_order_history')
        self.assertEqual(url, '/order/history')
        response = self.client.get(reverse('order:customer_order_history'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/order/history')
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_cancellation(self):
        '''
        Test that the url for the customer cancellation is correct.
        '''
        url = reverse('order:customer_cancellation')
        self.assertEqual(url, '/order/cancellation')
        response = self.client.get(reverse('order:customer_cancellation'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/order/cancellation')
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_returns(self):
        '''
        Test that the url for the customer returns is correct.
        '''
        url = reverse('order:customer_returns')
        self.assertEqual(url, '/order/returns')
        response = self.client.get(reverse('order:customer_returns'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/order/returns')
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_order_complete(self):
        '''
        Test that the url for the customer order complete is correct.
        '''
        url = reverse('order:order_complete')
        self.assertEqual(url, '/order/confirmation')
        response = self.client.get(reverse('order:order_complete'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/order/confirmation')
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_customer_checkout(self):
        '''
        Test that the url for the customer checkout is correct.
        '''
        url = reverse('order:checkout')
        self.assertEqual(url, '/order/checkout')
        response = self.client.get(reverse('order:checkout'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/order/checkout')
        self.assertEqual(response.status_code, 302)

from django.urls import reverse
from django.test import TestCase, override_settings


class TestReviewUrls(TestCase):
    '''
    Test suite for review modules.
    '''

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_review_list_url(self):
        '''
        Test case for review history url.
        '''
        url = reverse('customer_review_history')
        self.assertEqual(url, '/review/')
        response = self.client.get(reverse('customer_review_history'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/review/')
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_unreview_list_url(self):
        '''
        Test case for unreview history url.
        '''
        url = reverse('customer_to_be_reviewed')
        self.assertEqual(url, '/review/pending/')
        response = self.client.get(reverse('customer_to_be_reviewed'))
        self.assertRedirects(response, reverse('customer_sign_in') + '?next=/review/pending/')
        self.assertEqual(response.status_code, 302)

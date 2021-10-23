from django.test import TestCase, override_settings
from django.urls import reverse


class HomeTestsUrls(TestCase):
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_home_url(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_about_url(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_contact_url(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

from django.test import TestCase
from newsletter.models import Subscriber


class NewsletterModelTest(TestCase):
    """ Test suite for customer model """

    def setUp(self):
        """ Set up test database """
        Subscriber.objects.create(email='test@gmail.com', confirmed=True)
        Subscriber.objects.create(email='test2@gmail.com', confirmed=False)

    def tearDown(self):
        """ Clean up test database """
        Subscriber.objects.all().delete()

    def test_string_representation(self):
        """ Test string representation of model """
        email = Subscriber.objects.get(email='test@gmail.com')
        self.assertEqual(str(email), 'test@gmail.com (confirmed)')

    def test_unconfirmed_string_representation(self):
        """ Test string representation of unconfirmed model """
        email = Subscriber.objects.get(email='test2@gmail.com')
        self.assertEqual(str(email), 'test2@gmail.com (not confirmed)')

    def test_subscriber_confirmed(self):
        """ Test confirmed field """
        confirmed = Subscriber.objects.filter(email='test@gmail.com', confirmed=True)
        self.assertEqual(confirmed.count(), 1)

    def test_subscriber_unconfirmed(self):
        """ Test unconfirmed field """
        unconfirmed = Subscriber.objects.filter(email='test@gmail.com', confirmed=False)
        self.assertEqual(unconfirmed.count(), 0)

    def test_subscriber_verbose_name(self):
        """ Test verbose name of model """
        self.assertEqual(str(Subscriber._meta.verbose_name), 'Subscriber')

    def test_subscriber_verbose_name_plural(self):
        """ Test verbose name of model """
        self.assertEqual(str(Subscriber._meta.verbose_name_plural), 'Subscribers')

from django.test import TestCase
from customers.models import Customer, User


class CustomerTestCase(TestCase):
    """ Test module for customer model """

    def setUp(self):
        """ Set up test database """
        user = User.objects.create_user(
            email="john@example.com",
            password="password",
            is_staff=True,
            is_superuser=False,
            is_active=True,
            is_customer=True
        )
        Customer.objects.create(
            user=user,
            full_name="John Doe",
            email="john@example.com",
            phone_number="+8801761249108",
            address="123 Fake Street, London, UK",
            country="UK",
        )

    def tearDown(self):
        """ Tear down test database """
        Customer.objects.all().delete()
        User.objects.all().delete()

    def test_customer_email(self):
        """ Test customer email """
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.email, "john@example.com")

    def test_customer_invalid_email(self):
        """Test creating customer with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, password="password")

    def test_customer_email_normalized(self):
        """ Test email is normalized """
        email = "john@example.com"
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.email, email.lower())

    def test_customer_full_name(self):
        """ Test customer full name """
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.full_name, "John Doe")

    def test_customer_phone_number(self):
        """ Test customer phone number """
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.phone_number, "+8801761249108")

    def test_customer_address(self):
        """ Test customer address """
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.address, "123 Fake Street, London, UK")

    def test_customer_country(self):
        """ Test customer country """
        customer = Customer.objects.get(full_name="John Doe")
        self.assertEqual(customer.country, "UK")

    def test_user_is_active(self):
        """ Test user is active """
        user = User.objects.get(email="john@example.com")
        self.assertTrue(user.is_active)

    def test_user_is_customer(self):
        """ Test user is_customer=True """
        user = User.objects.get(email="john@example.com")
        self.assertTrue(user.is_customer)

    def test_user_is_not_superuser(self):
        """ Test user is not a superuser """
        user = User.objects.get(email="john@example.com")
        self.assertFalse(user.is_superuser)

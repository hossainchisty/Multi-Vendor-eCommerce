from django.test import TestCase
from customers.forms import CustomerSignUpForm
from customers.models import Customer, User


class TestCustomerFormTest(TestCase):
    """ Test suite for customer form """

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

# def test_valid_form(self):
#     ''' Test valid form '''
#     form = CustomerSignUpForm(
#         {
#             'full_name': 'John Doe',
#             'email': 'john@gmail.com',
#             'phone_number': '+8801234567890',
#             'address': '123 Main St',
#             'country': 'United States',
#             'password1': 'password',
#             'password2': 'password',
#         },
#     )
#     self.assertTrue(form.is_valid())
#     customer = form.save()
#     self.assertEqual(customer.full_name, 'John Doe')
#     self.assertEqual(customer.email, 'jon@gmail.com')
#     self.assertEqual(customer.phone_number, '+8801234567890')
#     self.assertEqual(customer.address, '123 Main St')
#     self.assertEqual(customer.country, 'United States')
#     self.assertEqual(customer.user.is_staff, False)
#     self.assertEqual(customer.user.is_superuser, False)
#     self.assertEqual(customer.user.is_active, True)
#     self.assertEqual(customer.user.is_customer, True)
#     self.assertEqual(customer.user.is_vendor, False)

    def test_invalid_form(self):
        form = CustomerSignUpForm(
            {
                'full_name': 'John Doe',
                'email': 'john@gmail.com',
                'phone_number': '+88017124567890',
                'address': '123 Main St',
                'country': 'United States',
                'password1': 'password',
                'password2': 'password',
            }
        )
        self.assertFalse(form.is_valid())

    def test_invalid_form_missing_fields(self):
        form = CustomerSignUpForm(
            {
                'full_name': 'John Doe',
                'email': '',
                'phone_number': '+88017124567890',
                'address': '123 Main St',
                'country': 'United States',
                'password1': 'password',
                'password2': 'password',
            }
        )
        self.assertFalse(form.is_valid())

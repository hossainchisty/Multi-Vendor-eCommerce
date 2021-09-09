from customers.models import User
from django.test import TestCase, TransactionTestCase
from product.models import Product
from vendor.models import Vendor


class VendorTestCase(TransactionTestCase):
    """Test module for vendor model"""

    def setUp(self):
        """Set up test database"""
        user = User.objects.create_user(
            email="john@example.com",
            password="password",
            is_staff=True,
            is_superuser=False,
            is_active=True,
            is_customer=False,
            is_vendor=True,
        )
        Vendor.objects.create(
            user=user,
            vendor_name="Vendor 1",
            owner_name="John Doe",
            nid_number="123456789",
            mobile_number="+8801788765432",
            email="john@example.com",
            address="Address 1",
        )

    def tearDown(self):
        """Tear down test database"""
        Vendor.objects.all().delete()
        User.objects.all().delete()

    def test_vendor_name(self):
        """Test vendor name"""
        vendor = Vendor.objects.get(vendor_name="Vendor 1")
        self.assertEqual(vendor.vendor_name, "Vendor 1")

    def test_vendor_owner_name(self):
        """Test vendor name"""
        vendor = Vendor.objects.get(vendor_name="Vendor 1")
        self.assertEqual(vendor.owner_name, "John Doe")

    def test_vendor_nid_number(self):
        """Test	vendor nid number"""
        vendor = Vendor.objects.get(vendor_name="Vendor 1")
        self.assertEqual(vendor.nid_number, "123456789")

    def test_vendor_mobile_number(self):
        """Test vendor mobile number"""
        vendor = Vendor.objects.get(vendor_name="Vendor 1")
        self.assertEqual(vendor.mobile_number, "+8801788765432")

    def test_vendor_address(self):
        """Test vendor address"""
        vendor = Vendor.objects.get(vendor_name="Vendor 1")
        self.assertEqual(vendor.address, "Address 1")

    def test_vendor_email_normalized(self):
        """Test the email for a new vendor is normalized"""
        email = "john@example.com"
        vendor = Vendor.objects.get(vendor_name="Vendor 1")
        self.assertEqual(vendor.email, email.lower())

    def test_vendor_invalid_email(self):
        """Test creating vendor with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, password="password")

    def test_user_is_active(self):
        """ Test user is active """
        user = User.objects.get(email="john@example.com")
        self.assertTrue(user.is_active)

    def test_user_is_vendor(self):
        """ Test user is_vendor=True """
        user = User.objects.get(email="john@example.com")
        self.assertTrue(user.is_vendor)

    def test_user_is_not_superuser(self):
        """ Test user is not a superuser """
        user = User.objects.get(email="john@example.com")
        self.assertFalse(user.is_superuser)

    def test_verbose_name_plural(self):
        """Test the plural name of vendor"""
        self.assertEqual(str(Vendor._meta.verbose_name_plural), "Vendors")

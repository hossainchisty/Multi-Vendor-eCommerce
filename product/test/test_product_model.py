import unittest

from customers.models import User
from django.test import Client, TestCase, TransactionTestCase
from product.models import Category, Product
from vendor.models import Vendor

# test runser, assertion libary, headless browser


class ProductTestCase(TransactionTestCase):
    """ Test module for product model """

    def setUp(self):
        """ Set up the test """
        user = User.objects.create_user(
            email="john@example.com",
            password="password",
            is_staff=True,
            is_superuser=False,
            is_active=True,
            is_vendor=True,
        )
        vendor = Vendor.objects.create(
            user=user,
            vendor_name='Test vendor',
            owner_name='Test owner',
            shop_logo='image.png',
            email='admin@gmail.com',
        )
        Category.objects.create(title='Test Category')
        Product.objects.create(
            title='Test Product',
            description='This is a test product',
            price=100.00,
            discount=07.00,
            category=Category.objects.get(title='Test Category'),
            created_by=vendor,
            available=True,
            is_new=True
        )

    def tearDown(self):
        """ Tear down the test """
        Product.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()
        Vendor.objects.all().delete()

    def test_product_price_is_correct(self):
        """ Test that the product price is correct """
        product = Product.objects.get(
            title='Test Product'
        )
        self.assertEqual(product.price, 100.00)

    def test_product_is_discount(self):
        """ Test that the product is discounted """
        product = Product.objects.get(
            title='Test Product',)
        self.assertEqual(product.discount, 07.00)

    def test_product_title_is_correct(self):
        """ Test that the product title is correct """
        product = Product.objects.get(
            title='Test Product',

        )
        self.assertEqual(product.title, 'Test Product')

    def test_product_description_is_correct(self):
        """ Test that the product description is correct """

        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.description, 'This is a test product')

    def test_product_available(self):
        """ Test that the product is available """

        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.available, True)

    def test_product_is_not_available(self):
        """ Test that the product is not available """
        product = Product.objects.get(title='Test Product')
        self.assertTrue(product.available)

    def test_product_is_new(self):
        """ Test that the product is new """
        product = Product.objects.get(
            title='Test Product',

        )
        self.assertEqual(product.is_new, True)

    def test_product_str(self):
        """Test the product string representation"""
        product = Product.objects.get(title='Test Product')
        self.assertEqual(str(product), product.title)

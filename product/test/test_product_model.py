from django.template.defaultfilters import slugify
from django.test import TransactionTestCase

from product.models import Category, Product
from vendor.models import Vendor
from customers.models import User


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
            available=True,
            is_new=True,
            rating=4.50,
            numbersOfReview=100,
            countInStock=2000,
            category=Category.objects.get(title='Test Category'),
            created_by=vendor,
        )

    def tearDown(self):
        """ Tear down the test """
        Product.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()
        Vendor.objects.all().delete()

    def test_product_title(self):
        """ Test that the product title is correct """
        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.title, 'Test Product')

    def test_product_slug(self):
        """Test the slug of the product"""
        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.slug, slugify(product.title))

    def test_product_is_in_stock(self):
        """Test that the product is in stock"""
        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.countInStock, 2000)

    def test_product_rating(self):
        """Test the product rating"""
        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.rating, 4.50)

    def test_product_numbers_of_review(self):
        """Test the numbers of review of the product"""
        product = Product.objects.get(title='Test Product')
        self.assertEqual(product.numbersOfReview, 100)

    def test_product_price(self):
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

    def test_product_description(self):
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

    def test_category_str(self):
        """Test the category string representation"""
        category = Category.objects.get(title='Test Category')
        self.assertEqual(str(category), category.title)

    def test_verbose_name_plural(self):
        """Test the plural name of the product"""
        self.assertEqual(str(Product._meta.verbose_name_plural), "Products")

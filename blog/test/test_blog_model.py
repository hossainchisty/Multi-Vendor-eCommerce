from django.test import TestCase
from customers.models import User, Customer
from blog.models import Post, Category, Comment


class TestPostCase(TestCase):
    '''
    Test suite for post model
    '''

    def setUp(self):
        '''
        Create a post instance for testing
        '''
        user = User.objects.create_user(
            email="john@example.com",
            password="password",
            is_staff=True,
            is_superuser=False,
            is_active=True,
            is_customer=True
        )
        category = Category.objects.create(name='python', slug='python')
        Post.objects.create(title='test title', slug='test-slug', content='test content', category=category, author=user, is_published=True)

    def tearDown(self):
        '''
        Delete the post instance after testing
        '''
        Post.objects.all().delete()
        Category.objects.all().delete()

    def test_string_representation(self):
        '''
        Test the string representation of the post
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(str(post), 'test title')

    def test_verbose_name_plural(self):
        '''
        Test the post verbose name and plural
        '''
        self.assertEqual(str(Post._meta.verbose_name_plural), 'Blogs')

    def test_post_title(self):
        '''
        Test the post title
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(post.title, 'test title')

    def test_post_slug(self):
        '''
        Test the post slug
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(post.slug, 'test-slug')

    def test_post_is_published(self):
        '''
        Test the post is_published = True
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(post.is_published, True)

    def test_post_category(self):
        '''
        Test the post category
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(post.category.name, 'python')
        self.assertEqual(post.category.slug, 'python')

    def test_post_author(self):
        '''
        Test the post author
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(post.author.email, 'john@example.com')

    def test_post_content(self):
        '''
        Test the post content
        '''
        post = Post.objects.get(title='test title')
        self.assertEqual(post.title, 'test title')
        self.assertEqual(post.slug, 'test-slug')
        self.assertEqual(post.content, 'test content')


class TestCommentModel(TestCase):
    '''
    Test suite for the comment model
    '''

    def setUp(self):
        '''
        Create a comment instance for testing
        '''
        user = User.objects.create_user(
            email="john@example.com",
            password="password",
            is_staff=True,
            is_superuser=False,
            is_active=True,
            is_customer=True
        )
        who_commented = Customer.objects.create(
            user=user,
            full_name="John Doe",
            email="john@example.com",
            phone_number="+8801761249108",
            address="123 Fake Street, London, UK",
            country="UK",
        )
        category = Category.objects.create(name='Test Category')
        post = Post.objects.create(title='Test Post', slug='test-post', content='Test Content', author=user, category=category, )
        Comment.objects.create(post=post, customer=who_commented, body='Test Comment')

    def tearDown(self):
        '''
        Delete the post instance after testing
        '''
        Post.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

    def test_comment_model(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.body, 'Test Comment')
        self.assertEqual(comment.customer.email, 'john@example.com')
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.post.slug, 'test-post')
        self.assertEqual(comment.post.author.email, 'john@example.com')

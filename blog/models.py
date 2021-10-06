from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django.utils import timezone
from customers.models import User, Customer
from django.db import models
from django.urls import reverse
from model.common_fields import BaseModel


class Category(models.Model):
    ''' Category for published posts. '''
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(BaseModel):
    ''' Represents a post in the blog application. '''
    class PublishedManager(models.Manager):
        ''' Custom manager for published posts. '''

        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Custom manager

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    is_published = models.BooleanField(default=False)
    image = CloudinaryField('image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tags = TaggableManager()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Blogs'

    def recent_post(self):
        ''' Returns the most recent post. '''
        self.is_published = True
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Comment(BaseModel):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Comment by {customer.full_name} on - {post.title}'

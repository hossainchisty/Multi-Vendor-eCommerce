"""
Title: Multi vendor eCommerce software application
Description: Multi-seller e-commerce platform.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty
"""

from pathlib import Path

import cloudinary
import cloudinary.api
import cloudinary.uploader
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

# cloudinary configration
cloudinary.config(cloud_name="hossainchisty", api_key="958916513788356",
                  api_secret="2BaQjUoM5jHa3K6VVpbaSs_icBQ")

SECRET_KEY = 'django-insecure-aw5k1oe@$nupmyzx+u1$+)a#@*b8ltdkp+q=&pg5q@=fl&8ims'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'cloudinary',
    'django_countries',
    'crispy_forms',
    'taggit',
    'captcha',
    # local apps
    'core.apps.CoreConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'review.apps.ReviewConfig',
    'product.apps.ProductConfig',
    'vendor.apps.VendorConfig',
    'blog.apps.BlogConfig',
    'customers.apps.CustomersConfig',
    'wishlist.apps.WishlistConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

SITE_ID = 1
WSGI_APPLICATION = 'Project.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = "customers.User"

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = "bootstrap4"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'static']

# Mail configrations
EMAIL_HOST = "smtp.zoho.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "hossain.chisty@zohomail.com"
EMAIL_HOST_PASSWORD = "#2#3B399TiU@aBC"
EMAIL_USE_SSL = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Google reCAPTCHA
RECAPTCHA_PUBLIC_KEY = '6LdDdJYcAAAAAF8MaL1PGHRCnkoSGsNuDaQ1bCXD'
RECAPTCHA_PRIVATE_KEY = '6LdDdJYcAAAAAEpnhcFoqjVfLmTvTcFU_EiSaD6z'

# Session configuration
CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 86400  # 24 hours in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Celery Configurations
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Dhaka'

LOGIN_URL = 'customer_sign_in'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'customer_sign_out'
LOGOUT_REDIRECT_URL = 'customer_sign_in'


# Activate Django-Heroku.
django_heroku.settings(locals())

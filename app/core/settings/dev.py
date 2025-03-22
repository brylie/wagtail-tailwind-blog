from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-57hsn%1u@e361a!ix-f^4@tp^_01h%q%8#oy$_%h2_k+$q*n*^"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .base import *
except ImportError:
    pass

# Set middleware based on the base.middleware without the XFrameOptionsMiddleware
MIDDLEWARE = [
    item for item in MIDDLEWARE if item != "django.middleware.clickjacking.XFrameOptionsMiddleware"
]
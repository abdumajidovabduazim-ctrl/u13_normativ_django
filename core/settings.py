"""
Django settings for core project.
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# LOCALE
# =========================
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# =========================
# SECURITY
# =========================
SECRET_KEY = 'django-insecure-9p5539l#jf^9tn6-%%0n*vijipw1*4vp-@d_*k1)3+koq01+nx'
DEBUG = True
ALLOWED_HOSTS = []

# =========================
# APPS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # sites (MUHIM)
    'django.contrib.sites',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # local apps
    'shop',
    'posts',
    'accounts',
    'post',

    # 'accounts.apps.AccountsConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_yasg',

]

SITE_ID = 1

# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # 👇 MUHIM: shu yerga qo'yiladi
    'allauth.account.middleware.AccountMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'accounts.middleware.RequestLoggerMiddleware',
]

# =========================
# AUTH BACKENDS (MUHIM)
# =========================
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# =========================
# URLS
# =========================
ROOT_URLCONF = 'core.urls'

# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# =========================
# DATABASE
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('uz', 'Uzbek'),
]

# =========================
# STATIC
# =========================
STATIC_URL = 'static/'

# =========================
# DEFAULT PK
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# EMAIL
# =========================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

EMAIL_HOST_USER = 'abdumajidovabduazim@gmail.com'
EMAIL_HOST_PASSWORD = 'sgsh nsio rihv wwoo'

# =========================
# LOGGING
# =========================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'fayl': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'requests.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'request_logger': {
            'handlers': ['fayl'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],

    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],

    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",

    "PAGE_SIZE": 5,
}
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Bearer <JWT token>",
        }
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
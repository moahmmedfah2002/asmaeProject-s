import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uxprsdhk^gzd-r=_287byolxn)$k6tsd8_cepl^s^tms2w1qrv'

# Default site settings
DEFAULT_HOST = 'http://localhost:8000'
DEFAULT_HOST = 'http://127.0.0.1:8000'
ALLOWED_HOSTS = ['*']
LOGGING = {
    'version': 1,  # REQUIRED
    'disable_existing_loggers': False,
    'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
    },
},
'loggers': {
    'django': {
        'handlers': ['console'],  # Log to terminal instead
        'level': 'DEBUG',
    }
}
}
# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'janeway'),
        'USER': os.environ.get('DB_USER', 'janeway'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'janeway'),
        'HOST': os.environ.get('DB_HOST', 'janeway-postgres'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Email Configuration
EMAIL_BACKEND = os.environ.get('JANEWAY_EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('JANEWAY_EMAIL_HOST', 'janeway-debug-smtp')
EMAIL_PORT = int(os.environ.get('JANEWAY_EMAIL_PORT', 1025))
EMAIL_USE_TLS = os.environ.get('JANEWAY_EMAIL_USE_TLS', 'False').lower() == 'true'

# Application settings
INSTALLED_APPS = [
    
  
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files
STATIC_URL = '/static/'
SITE_URL = 'http://localhost:8000'
SITE_URL = 'http://127.0.0.1:8000'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SECURE_PROXY_SSL_HEADER = None

# Default language
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Login URL
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/user/profile/'

# CAPTCHA configuration
CAPTCHA_TYPE = 'recaptcha'  # 'simple_math', 'recaptcha', or 'hcaptcha'

# ReCaptcha keys
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_PUBLIC_KEY = ''

# HCaptcha keys
HCAPTCHA_SITEKEY = ''
HCAPTCHA_SECRET = ''

# ORCID Configuration
ENABLE_ORCID = True
ORCID_API_URL = 'http://pub.orcid.org/v1.2_rc7/'
ORCID_URL = 'https://orcid.org/oauth/authorize'
ORCID_TOKEN_URL = 'https://pub.orcid.org/oauth/token'
ORCID_CLIENT_SECRET = ''
ORCID_CLIENT_ID = ''

# URL configuration
URL_CONFIG = 'path'  # 'path' or 'domain'

# OIDC Authentication Settings
ENABLE_OIDC = False
OIDC_SERVICE_NAME = 'OIDC Service Name'
OIDC_RP_CLIENT_ID = ''
OIDC_RP_CLIENT_SECRET = ''
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_OP_AUTHORIZATION_ENDPOINT = ''
OIDC_OP_TOKEN_ENDPOINT = ''
OIDC_OP_USER_ENDPOINT = ''
OIDC_OP_JWKS_ENDPOINT = ''

# Full-text search
ENABLE_FULL_TEXT_SEARCH = False
CORE_FILETEXT_MODEL = "core.FileText"  # Or "core.PGFileText" for Postgres

# PgAdmin
PGADMIN_PORT = 5050

# Janeway server port
JANEWAY_PORT = 8000

# Janeway Email Configuration
JANEWAY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
JANEWAY_EMAIL_HOST = 'janeway-debug-smtp'
JANEWAY_EMAIL_PORT = 1025
JANEWAY_EMAIL_USE_TLS = False

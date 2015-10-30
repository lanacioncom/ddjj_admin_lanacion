# coding: utf-8
"""
Django settings for admin_ddjj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'grappelli_nested',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_ddjj_app',
    'django_extensions',
    'debug_toolbar.apps.DebugToolbarConfig',
    'rest_framework',
    'api',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'admin_ddjj.urls'

#WSGI_APPLICATION = 'admin_ddjj.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-AR'
NUMBER_GROUPING = 3
USE_THOUSAND_SEPARATOR = True
DECIMAL_SEPARATOR = ','

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GRAPPELLI_ADMIN_TITLE = "La Nación - Declaraciones Juradas"



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

TEMPLATE_DIRS = (
     os.path.join(BASE_DIR, 'templates'),
)

BACKEND_BASE_URL = "http://ddjj.lanacion.com.ar/"
FRONTEND_BASE_URL = "http://interactivos.lanacion.com.ar/declaraciones-juradas"

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_METHODS = (
        'GET',
        'OPTIONS'
)
 
try:
    from local_settings import *
except ImportError:
    pass

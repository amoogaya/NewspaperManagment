"""
Django settings for NewspaperManagment project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6&j(&vnw+qu_%=#cmj4&pxy7@mm%0t51gh_)9_@99!x2si6-cy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newspaper.apps.NewspaperConfig',

    'accounts.apps.AccountsConfig',
    'djrichtextfield',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

]

ROOT_URLCONF = 'NewspaperManagment.urls'

# DJRICHTEXTFIELD_CONFIG = {
#     'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
#
#     'css': {
#         # 'all': [
#         #   'https://cdn.example.com/css/editor.css'
#         # ]
#     },
#
#     'init_template': 'djrichtextfield/init/tinymce.js',
#     'settings': {  # TinyMCE
#         'menubar': False,
#         'plugins': 'link image table code',
#         'toolbar': 'bold italic | link image | removeformat |formatselect | table ',
#         'width': 700
#     },
#     'profiles': {
#         'basic': {
#             'toolbar': 'bold italic | removeformat'
#         },
#         'advanced': {
#             'plugins': 'link image table code',
#             'toolbar': 'format select | bold italic | removeformat |'
#                        ' link unlink image table | code'
#         },
#     }
#
# }

DJRICHTEXTFIELD_CONFIG = {
    'js': [
        '//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js',
        '//cdnjs.cloudflare.com/ajax/libs/summernote/0.8.9/summernote-lite.js',
    ],
    'css': {
        'all': [
            '//cdnjs.cloudflare.com/ajax/libs/summernote/0.8.9/summernote-lite.css',
        ]
    },
    'init_template': 'rich_text/summernote_init.js',
    'settings': {
        'followingToolbar': False,
        'minHeight': 250,
        'width': 700,
        'toolbar': [
            ['style', ['bold', 'italic', 'clear']],
        ],
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'NewspaperManagment.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'newspaper.MyUser'

WAGTAIL_SITE_NAME = 'My Example Site'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

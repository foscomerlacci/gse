"""
Django settings for gse project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'le!i=r9&#dib5g!kp!$54&j1-38)h73(y(tr0&bi#ww#5dx+3l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (

    # 'django_admin_select2',
    'dbbackup',  # django-dbbackup

    # 'flat_responsive', # only if django version < 2.0
    # 'flat', # only if django version < 1.9
    'colorfield',
    # 'smart_selects',
    # 'multiupload',
    # 'easy_thumbnails',
    # 'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    # 'admin_tools.dashboard',
    # 'mptt',

    'jquery',
    'requests',
    'anagrafica',
    'dispositivi',
    'interventi',
    'prestiti',
    'admin_interface',
    # 'jet',
    # 'jet.dashboard',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crequest',

    # 'assegnazioni',

    # 'filer',
    # 'django_select2',



)

MIDDLEWARE= (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'crequest.middleware.CrequestMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'prestiti.request_exposer.RequestExposerMiddleware',

)

ROOT_URLCONF = 'gse.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),

                 ],
        # 'DIRS':'admin_tools.template_loaders.Loader',

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'gse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'gse.sqlite3'),
        'ATOMIC_REQUESTS': 'True',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'it-IT'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # '/static/admin/css/',
    'gse/static'
    # os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = '/home/utente/PycharmProjects/gse/static'
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       'django.contrib.staticfiles.finders.FileSystemFinder',)

                       # Media

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MAX_UPLOAD_SIZE = 5120000    # max uploadable = 5 MB

JQUERY_URL = True



THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    # 'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    # 'easy_thumbnails.processors.filters',
)

# configurazione JET

# JET_THEMES = [
#     {
#         'theme': 'default', # theme folder name
#         'color': '#47bac1', # color of the theme's button in user menu
#         'title': 'Default' # theme title
#     },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     {
#         'theme': 'light-green',
#         'color': '#2faa60',
#         'title': 'Light Green'
#     },
#     {
#         'theme': 'light-violet',
#         'color': '#a464c4',
#         'title': 'Light Violet'
#     },
#     {
#         'theme': 'light-blue',
#         'color': '#5EADDE',
#         'title': 'Light Blue'
#     },
#     {
#         'theme': 'light-gray',
#         'color': '#222',
#         'title': 'Light Gray'
#     }
# ]
#
#
# JET_SIDE_MENU_COMPACT = True
# JET_DEFAULT_THEME = 'light-gray'
# JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'
# JET_CHANGE_FORM_SIBLING_LINKS = False


# JET_SIDE_MENU_ITEMS = [
#
#     {'label':' ','app_label': 'anagrafica', 'items': [
#         {'name': 'utente'},
#     ]},
#
#     {'label':' ','app_label': 'dispositivi', 'items': [
#         {'name': 'dispositivo'},
#     ]},
#
#     {'app_label': 'auth', 'items': [
#         {'name': 'group'},
#         {'name': 'user'},
#     ]},
#
# ]
#
# JET_SIDE_MENU_ITEMS = [
#     {'label':' ','app_label': 'anagrafica', 'items': [
#         {'name': 'utente'},
#     ]},
#     # {'app_label': 'auth', 'items': [
#     #     {'name': 'group'},
#     #     {'name': 'user'},
#     # ]},
#     {'label':' ','app_label': 'dispositivi', 'items': [
#         {'name': 'dispositivo'},
#     ]},
# ]


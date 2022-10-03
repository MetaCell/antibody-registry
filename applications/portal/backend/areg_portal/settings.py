"""
Django settings for the MNP Checkout project.
Generated by 'django-admin startproject' using Django 3.2.12.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-81kv$0=07xac7r(pgz6ndb5t0at4-z@ae6&f@u6_3jo&9d#4kl"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("PRODUCTION", None) else True

ALLOWED_HOSTS = [
    "*",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cloudharness.middleware.django.CloudharnessMiddleware",
]

ROOT_URLCONF = "areg_portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "areg_portal.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PROJECT_NAME = "areg_portal".upper()

# Persistent storage
PERSISTENT_ROOT = os.path.join(BASE_DIR, "persistent")

# ***********************************************************************
# * areg_portal settings
# ***********************************************************************
from cloudharness.applications import get_configuration
from cloudharness.utils.config import ALLVALUES_PATH, CloudharnessConfig

# ***********************************************************************
# * import base CloudHarness Django settings
# ***********************************************************************
from cloudharness_django.settings import *

# add the local apps
INSTALLED_APPS += [
    "api",
    "areg_portal"
]

# override django admin base template with a local template
# to add some custom styling
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

# Static files (CSS, JavaScript, Images)
MEDIA_ROOT = PERSISTENT_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

# KC Client & roles
KC_CLIENT_NAME = PROJECT_NAME.lower()

# areg_portal specific roles

# Default KC roles
KC_ADMIN_ROLE = f"administrator"  # admin user
KC_MANAGER_ROLE = f"manager"  # manager user
KC_USER_ROLE = f"user"  # customer user
KC_ALL_ROLES = [
    KC_ADMIN_ROLE,
    KC_MANAGER_ROLE,
    KC_USER_ROLE,
]
KC_PRIVILEGED_ROLES = [
    KC_ADMIN_ROLE,
    KC_MANAGER_ROLE,
]

KC_DEFAULT_USER_ROLE = None  # don't add the user role to the realm default role

# Database models settings

# comment refers to max length of column at ingestion time (12/09/2022)
ANTIBODY_NAME_MAX_LEN = 512  # 352
ANTIBODY_TARGET_MAX_LEN = 1024  # 783
ANTIBODY_TARGET_SPECIES_MAX_LEN = 4096  # 2047
VENDOR_MAX_LEN = 512  # 200
ANTIBODY_CATALOG_NUMBER_MAX_LEN = 256  # 165
ANTIBODY_CLONALITY_MAX_LEN = 32
ANTIBODY_CLONE_ID_MAX_LEN = 256  # 150
URL_MAX_LEN = 2048  # 938
ANTIGEN_ENTREZ_ID_MAX_LEN = 2048  # 1383
ANTIBODY_PRODUCT_ISOTYPE_MAX_LEN = 256  # 150
ANTIBODY_PRODUCT_CONJUGATE_MAX_LEN = 512  # 285
ANTIBODY_PRODUCT_FORM_MAX_LEN = 1024  # 802
ANTIBODY_TARGET_SUBREGION_MAX_LEN = 256  # 221
ANTIBODY_TARGET_MODIFICATION_MAX_LEN = 128  # 67
ANTIBODY_DEFINING_CITATION_MAX_LEN = 16384  # 9206
ANTIBODY_DISC_DATE_MAX_LEN = 128  # 85
ANTIBODY_ID_MAX_LEN = 32  # 8
STATUS_MAX_LEN = 8
ANTIBODY_CAT_ALT_MAX_LEN = 512  # 334
VENDOR_COMMERCIAL_TYPE_MAX_LEN = 10  # 10
ANTIGEN_UNIPROT_ID_MAX_LEN = 64  # 32
ANTIBODY_TARGET_EPITOPE_MAX_LEN = 1024  # 897
VENDOR_NIF_MAX_LEN = 32  # 14

ANTIBODY_ANTIBODY_START_SEQ = 3000000  # 2858735
ANTIBODY_VENDOR_DOMAIN_START_SEQ = 1000  # 813
ANTIBODY_VENDOR_START_SEQ = 20000  # 12233

RAW_ANTIBODY_DATA_BASENAME = 'antibody_table'
RAW_VENDOR_DATA_BASENAME = 'antibody_vendors'
RAW_VENDOR_DOMAIN_DATA_BASENAME = 'antibody_vendors_domain'
RAW_USERS_DATA_BASENAME = 'users_antibody'

CHUNK_SIZE = 10 ** 5

UID_KEY = 'uid'
GUID_KEY = 'guid'

ANTIBODY_HEADER = {'ab_name': "text", 'ab_target': "text", 'target_species': "text", 'vendor': "text",
                   'vendor_id': "int", 'catalog_num': "text", 'clonality': "text",
                   'source_organism': "text", 'clone_id': "text", 'url': "text", 'link': "text",
                   'ab_target_entrez_gid': "text", 'product_isotype': "text",
                   'product_conjugate': "text", 'product_form': "text", 'target_subregion': "text",
                   'target_modification': "text", 'comments': "text",
                   'feedback': "text", 'defining_citation': "text", 'disc_date': "text", 'curator_comment': "text",
                   'id': "text", 'ab_id': "text", 'ab_id_old': "text",
                   'of_record': "text", 'ix': "int", UID_KEY: "text", 'status': "text",
                   'insert_time': "text", 'curate_time': "text", 'cat_alt': "text", 'commercial_type': "text",
                   'uniprot_id': "text", 'epitope': "text", 'uid_legacy': "text"}

D_TYPES = ANTIBODY_HEADER.copy()
for dt in D_TYPES:
    if dt == 'int':
        D_TYPES[dt] = 'int64'
    else:
        D_TYPES[dt] = 'unicode'

MAX_TRIES = 10

ORCID_URL = "https://orcid.org/"

USERS_RELEVANT_HEADER = ['id', GUID_KEY, 'email', 'level', 'firstName', 'middleInitial', 'lastName', 'organization',
                         'created', 'orcid_id']

UID_INDEX = list(ANTIBODY_HEADER.keys()).index(UID_KEY)
GUID_INDEX = USERS_RELEVANT_HEADER.index(GUID_KEY)

DEFAULT_UID = '43'

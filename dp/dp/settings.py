import os

try:
    from .local_settings import *
except ImportError:
    pass

CURRENCY_URL_MAIN = "http://api.exchangeratesapi.io/v1/"
CURRENCY_RATE = 300

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIN_URL = "login"

SHOP_EMAILS_MANAGERS = ["angara77@gmail.com", "angara99@gmail.com"]
SHOP_EMAIL_FROM = "DucatoParts <partshub77@gmail.com>"
# SHOP_TEL = '8 (800) 302-53-50'
SHOP_TEL = "8 (495) 255-36-60"
# SHOP_TEL2 = '+7 (499) 380-78-08'
SHOP_TEL2 = ""
SHOP_TEL3 = "+7 (495) 255-36-60"

SHOP_ADDRESS_LINE_1 = "г.МОСКВА, ул. Горбунова 8 строение 1"
SHOP_ADDRESS_LINE_2 = "1 этаж"
SHOP_WORKING_HOURS = "Ежедневно с 9:00 до 19:00"
SHOP_WHATSAPP = "+7 (999) 858-26-58"
SHOP_SITE_HOST = "https://ducatoparts.ru"
SHOP_TEL_NO_BRACKETS = "+7-495-255-36-60"
BASE_URL = "https://ducatoparts.ru"
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240


SHOP_CONTACT_INFO = {
    "shop_email": SHOP_EMAIL_FROM,
    "shop_tel": SHOP_TEL,
    "shop_tel2": SHOP_TEL2,
    "shop_tel3": SHOP_TEL3,
    "shop_address": SHOP_ADDRESS_LINE_1 + " " + SHOP_ADDRESS_LINE_2,
    "shop_working_hours": SHOP_WORKING_HOURS,
    "address_line1": SHOP_ADDRESS_LINE_1,
    "address_line2": SHOP_ADDRESS_LINE_2,
    "shop_whatsapp": SHOP_WHATSAPP,
    "company_name": "АНГАРА77",
    "shop_tel_no_brackets": SHOP_TEL_NO_BRACKETS,
}


SALES_ON_SEARCH = [2274, 2582, 2027]
SALES_ON_HOME = {
    "brakes": [2774, 2582, 2560, 2027],
    "fuel": [1596, 3160, 1556, 1529],
    "body": [2257, 2252, 3508, 3757],
    "engine": [3136, 3035, 1932, 1027],
}

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False  # True
# DEBUG = True

ALLOWED_HOSTS = [
    "dp.loc",
    "localhost",
    "192.162.242.28",
    "ducatoparts.tk",
    "ducatoparts.ru",
    "enginexpert.ru",
]
SITE_URL = "https://ducatoparts.ru"

# Application definition
# commen

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "dp",
    "admin_ads_work",
    "products",
    "group_dict",
    "blogs",
    "home",
    "comments",
    "star_ratings",
    "accounts",
    "admin_photos",
    "email_form",
    "crispy_forms",
    "rest_framework",
    "interlink",
    "django_crontab",
    "currency",
]


CRONJOBS = [
    (
        "0 1 * * *",
        "currency.cron.run_api",
        ">> /home/manhee/ducatoparts.ru/dp/currency/cron.log",
    ),
]
ROOT_URLCONF = "cool_backend.urls"


SITE_ID = 1

CRISPY_TEMPLATE_PACK = "bootstrap3"

TAGS_LIST = [
    "задн",
    "передн",
    "лев",
    "прав",
    "внутр",
    "наружн",
    "верхн",
    "нижн",
    "боков",
    "коротк",
    "длинн",
    "всборе",
    "комплект",
    "низ",
    "верх",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dp.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates/base"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "dp.context_processor.small_cart",
                "dp.context_processor.sales_products",
                "dp.context_processor.contact_info",
            ],
        },
    },
]


WSGI_APPLICATION = "dp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": os.path.join(BASE_DIR, "dp/my.cnf"),
            "sql_mode": "traditional",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

USE_I18N = True
USE_L10N = False
LANGUAGE_CODE = "ru-RU"
USE_TZ = True
TIME_ZONE = "Europe/Moscow"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
IMG_ROOT = os.path.join(os.path.join(BASE_DIR, "static_root"), "img")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STAR_RATINGS_ANONYMOUS = True
STAR_RATINGS_RERATE = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp-relay.sendinblue.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "angara99@gmail.com"


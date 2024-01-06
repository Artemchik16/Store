import os
from pathlib import Path

import environ

# environ
env = environ.Env(
    SECRET_KEY=str,
    DEBUG=bool,
    ALLOWED_HOSTS=list,
    PG_DATABASE=str,
    PG_USER=str,
    PG_PASSWORD=str,
    DB_HOST=str,
    DB_PORT=int,
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# default apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]

# modern admin
INSTALLED_APPS.insert(0, "jazzmin")

# my apps
INSTALLED_APPS += [
    "api_v1.apps.ApiV1Config",
    "main.apps.MainConfig",
    "goods.apps.GoodsConfig",
    "users.apps.UsersConfig",
    "carts.apps.CartsConfig",
    "orders.apps.OrdersConfig",
]

#  other apps
INSTALLED_APPS += [
    "rest_framework",
    "django_filters",
    "debug_toolbar",

    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("PG_DATABASE"),
        "USER": env("PG_USER"),
        "PASSWORD": env("PG_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    },
    "extra": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}

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

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Almaty"

USE_I18N = True

USE_TZ = True

# static
STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]


# default redirect
LOGOUT_REDIRECT_URL = "users:login"
LOGIN_REDIRECT_URL = "goods:catalog_page"
LOGIN_URL = "users:login"

# Media files
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

# debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# jazzmin config ui
JAZZMIN_UI_TWEAKS = {
    "theme": "litera",
}

JAZZMIN_SETTINGS = {
    "topmenu_links": [
        {
            "name": "Админ-панель",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Главная",
            "url": "main:main_page",
            "new_window": True,
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Профиль",
            "url": "users:profile",
            "new_window": True,
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Каталог",
            "url": "goods:catalog_page",
            "new_window": True,
            "permissions": ["auth.view_user"],
        },
    ],
    "usermenu_links": [
        {
            "name": "Открыть сайт",
            "url": "main:main_page",
            "new_window": True,
            "permissions": ["auth.view_user"],
        },
    ],
}

###########################
# SPECTACULAR CONFIG
###########################
SPECTACULAR_SETTINGS = {
    "TITLE": "Shopy Shop",
    "DESCRIPTION": "Shopy Shop Documentation",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "SERVE_AUTHENTICATION": [
        "rest_framework.authentication.BasicAuthentication",
    ],
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayOperationId": True,
        "syntaxHighlight.active": True,
        "syntaxHighlight.theme": "arta",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "filter": True,
        "requestSnippetsEnabled": True,
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "SORT_OPERATIONS": False,
    "ENABLE_DJANGO_DEPLOY_CHECK": False,
    "DISABLE_ERRORS_AND_WARNINGS": True,
}
###########################

###########################
# DJANGO REST FRAMEWORK
###########################
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "api_v1.pagination.BasePagination",
}
###########################

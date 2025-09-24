import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if not DEBUG else ["*"]
CSRF_TRUSTED_ORIGINS = os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",") if not DEBUG else []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "registerbook"),
        "USER": os.environ.get("DB_USER", "registeruser"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

LANGUAGE_CODE = 'th'
TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'booksend' / 'static']

LOGIN_REDIRECT_URL = 'booksend_list'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
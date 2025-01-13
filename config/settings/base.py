import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
# ALLOWED_HOSTS = ["*"]

INSTALLED_APPS: tuple[str, ...] = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
)
MIDDLEWARE: tuple[str, ...] = (
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
)
# DATABASES: dict[str, dict[str, str]] = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": str(BASE_DIR / "db.sqlite3"),
#     }
# }

STATIC_URL = "/static/"

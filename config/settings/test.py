from typing import Mapping
from types import MappingProxyType

DEBUG = False
TESTING = True

DATABASES: Mapping[str, Mapping[str, str]] = MappingProxyType({
    "default": MappingProxyType({
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    })
})

PASSWORD_HASHERS: tuple[str, ...] = (
    "django.contrib.auth.hashers.MD5PasswordHasher",
)

SECRET_KEY = "test-secret-key"

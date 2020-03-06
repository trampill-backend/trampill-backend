from django.conf import settings

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="Ir9QdGjWuXbyyNxedxGpEGCJ20PYHImpPGiA0oKTri4edrzT5oxK6NzexZAoum90",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#         "LOCATION": "",
#     }
# }

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

# Your stuff...
# ------------------------------------------------------------------------------
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

NO_CACHE = -1
WHOLE_MODEL = 'whole-model'

CACHE_PREFIX = getattr(settings, 'CACHE_PREFIX', '')
FETCH_BY_ID = getattr(settings, 'FETCH_BY_ID', False)
FLUSH = CACHE_PREFIX + ':flush:'
CACHE_EMPTY_QUERYSETS = getattr(settings, 'CACHE_EMPTY_QUERYSETS', False)
TIMEOUT = getattr(settings, 'CACHE_COUNT_TIMEOUT', NO_CACHE)
CACHE_INVALIDATE_ON_CREATE = getattr(settings, 'CACHE_INVALIDATE_ON_CREATE', None)
CACHE_MACHINE_NO_INVALIDATION = getattr(settings, 'CACHE_MACHINE_NO_INVALIDATION', False)
CACHE_MACHINE_USE_REDIS = getattr(settings, 'CACHE_MACHINE_USE_REDIS', False)

_invalidate_on_create_values = (None, WHOLE_MODEL)
if CACHE_INVALIDATE_ON_CREATE not in _invalidate_on_create_values:
    raise ValueError('CACHE_INVALIDATE_ON_CREATE must be one of: ' '{}'.format(_invalidate_on_create_values))


MIDDLEWARE += [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

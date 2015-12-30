import ast
import logging
import os

from pkg_resources import working_set

logger = logging.getLogger(__name__)

ENTRY_POINT_API = 'powerplug.rest'
ENTRY_POINT_APP = 'powerplug.apps'
ENTRY_POINT_URL = 'powerplug.urls'
ENTRY_POINT_NAV = 'powerplug.subnav'


def add_urls(urlpatterns):
    from django.conf.urls import include, url
    for entry in working_set.iter_entry_points(ENTRY_POINT_URL):
        try:
            urlpatterns.append(
                url(r'^{0}/'.format(entry.name), include(entry.module_name, namespace=entry.name))
            )
        except ImportError:
            logger.exception('Error importing %s', entry.name)


def add_apis(urlpatterns):
    from django.conf.urls import include, url
    from rest_framework import routers
    router = routers.DefaultRouter()
    for entry in working_set.iter_entry_points(ENTRY_POINT_API):
        try:
            router.register(entry.name, entry.load())
        except ImportError:
            logger.exception('Error importing %s', entry.name)

    urlpatterns += url(r'^api/', include(router.urls, namespace='api')),


def add_apps(installed_apps):
    for entry in working_set.iter_entry_points(ENTRY_POINT_APP):
        if entry.module_name not in installed_apps:
            installed_apps += (entry.module_name,)
    return installed_apps


def environ(key, default=None):
    """
        Searches os.environ. If a key is found try evaluating its type else;
        return the string.
        returns: k->value (type as defined by ast.literal_eval)
    """
    # Taken from
    # https://github.com/mattseymour/python-env/blob/master/dotenv/__init__.py
    try:
        # Attempt to evaluate into python literal
        return ast.literal_eval(os.environ.get(key.upper(), default))
    except (ValueError, SyntaxError):
        return os.environ.get(key.upper(), default)

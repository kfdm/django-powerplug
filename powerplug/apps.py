import logging

from django.apps import AppConfig

from pkg_resources import working_set

logger = logging.getLogger(__name__)


class PowerplugConfig(AppConfig):
    name = 'powerplug'

    def ready(self):
        for entry in working_set.iter_entry_points('powerplug.signal'):
            try:
                entry.load()
            except ImportError:
                logger.exception('Error importing %s', entry.name)

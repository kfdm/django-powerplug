'''
Entry point for Celery tasks
'''

import logging

from pkg_resources import working_set

logger = logging.getLogger(__name__)

for entry in working_set.iter_entry_points('powerplug.task'):
    logger.info('Loading %s', entry)
    try:
        entry.load()
    except ImportError:
        logger.exception('Error importing %s', entry.name)

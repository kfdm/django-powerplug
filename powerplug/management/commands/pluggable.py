

from django.core.management.base import BaseCommand

from pkg_resources import working_set


class Command(BaseCommand):
    def handle(self, verbosity, **options):
        for entry_point, title in [
            ('powerplug.apps', 'Installed Apps'),
            ('powerplug.rest', 'Installed APIs'),
            ('powerplug.signal', 'Installed Signals'),
            ('powerplug.task', 'Installed Tasks'),
            ('powerplug.url', 'Installed URL'),
        ]:
            self.stdout.write(self.style.SUCCESS(title))
            for entry in working_set.iter_entry_points(entry_point):
                try:
                    entry.load()
                except ImportError as e:

                    self.stdout.write(self.style.ERROR('\t ' + str(entry)))
                    if verbosity > 0:
                        self.stdout.write(self.style.ERROR(e))
                else:
                    print('\t', entry)

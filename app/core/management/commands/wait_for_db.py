"""

Django commands for waiting for database
"""

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
import time

from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django wait for db command"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write('Database unaviable sleep for 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database aviable'))

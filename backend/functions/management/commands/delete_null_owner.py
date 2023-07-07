from django.core.management.base import BaseCommand
from functions.models import Function


class Command(BaseCommand):
    help = " delete functions have null owner "

    def handle(self, *args, **options):
        Function.objects.filter(owner=None).delete()
        self.stdout.write(
            self.style.SUCCESS("functions have None owner are deleted successfully.")
        )

from django.core.management.base import BaseCommand

from apps.animals.services.delete_animals import delete_animals


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--is-only-auto-generated",
            help="Delete only auto generated animals",
            action="store_true",
        )

    def handle(self, *args, **options):
        is_only_auto_generated: bool = options["is_only_auto_generated"]

        delete_animals(is_only_auto_generated=is_only_auto_generated)

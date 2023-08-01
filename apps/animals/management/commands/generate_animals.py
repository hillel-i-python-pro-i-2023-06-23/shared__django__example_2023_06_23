from django.core.management.base import BaseCommand

from apps.animals.services.generate_and_save_animals import generate_and_save_animals


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="How many animals do you want to generate?",
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        generate_and_save_animals(amount=amount)

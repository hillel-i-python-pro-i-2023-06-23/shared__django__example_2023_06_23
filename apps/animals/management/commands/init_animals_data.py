from django.core.management.base import BaseCommand

from apps.animals import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for kind_as_str in ("Dog", "Cat"):
            models.Kind.objects.get_or_create(name=kind_as_str)

        for color_as_str in ("Black", "White", "Gray"):
            models.Color.objects.get_or_create(value=color_as_str)

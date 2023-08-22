import logging
import random
from typing import Final, TypeAlias

from django.core.management.base import BaseCommand
from faker import Faker

from apps.travels import models

T_COUNTRY: TypeAlias = str

COUNTRIES: Final[set[T_COUNTRY]] = {
    "Ukraine",
    "Poland",
    "Germany",
    "France",
    "Spain",
    "Portugal",
    "Italy",
    "Greece",
    "Brazil",
}


class Command(BaseCommand):
    MINIMAL_AMOUNT_OF_TRAVELERS: Final[int] = 10

    def handle(self, *args, **options):
        logger = logging.getLogger("django")

        for country_as_str in COUNTRIES:
            models.Country.objects.get_or_create(name=country_as_str)
        logger.info(f"countries: {models.Country.objects.count()}")

        faker = Faker()
        faker.first_name()

        current_amount_of_humans = models.Traveler.objects.count()
        if (amount := (self.MINIMAL_AMOUNT_OF_TRAVELERS - current_amount_of_humans)) > 0:
            for _ in range(amount):
                models.Traveler.objects.create(
                    name=faker.first_name(),
                )

        logger.info(f"travelers: {models.Traveler.objects.count()}")

        max_visited_countries = len(COUNTRIES) // 2

        for traveler in models.Traveler.objects.all():
            if traveler.visited_countries.count() >= max_visited_countries:
                continue

            for _ in range(random.randint(1, max_visited_countries)):
                random_country_from_db = models.Country.objects.order_by("?").first()
                traveler.visited_countries.add(random_country_from_db)

        logger.info("Added visits to countries")

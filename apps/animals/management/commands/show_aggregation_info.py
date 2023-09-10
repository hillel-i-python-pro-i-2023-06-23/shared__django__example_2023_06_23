import logging

from django.core.management.base import BaseCommand
from django.db import models

from apps.animals import models as animals_models


def show_aggregation_info():
    logger = logging.getLogger("django")
    logger.info("start")

    queryset_animals = animals_models.Animal.objects.all()

    # https://docs.djangoproject.com/en/4.2/topics/db/aggregation/

    # Aggregation.
    # Get some summary data for queryset at database level.

    logger.info("Aggregation")

    data__aggregate = queryset_animals.aggregate(
        models.Sum("age"),
        models.Avg("age"),
        models.Max("age"),
        models.Min("age"),
        # Sometimes it is useful to explicitly specify the name of a generated aggregate column.
        custom_name_for_count=models.Count("age"),
    )

    logger.info(f"{data__aggregate=}")

    logger.info(f"{queryset_animals.count()=}")
    logger.info(f"{len(queryset_animals)=}")

    # Annotation.
    # Calculate some data for each item in queryset.
    # Nested queries (field1__field2) allowed.

    logger.info("Annotation")

    data__annotate = queryset_animals.annotate(
        # Calculate the age plus 10 for each animal. "F" - field.
        age_plus_10=models.F("age") + 10,
        # Related calculations.
        colors_count=models.Count("colors"),
    )

    logger.info(f"{data__annotate.count()=}")
    # Limit the number of items in queryset.
    data__annotate__limited = data__annotate[:5]
    for item in data__annotate__limited:
        logger.info(f"{item=}")
        logger.info(f"{item.age=} - {item.age_plus_10=}")
        logger.info(f"{item.colors_count=}")

    # Annotation + Aggregation.

    logger.info("Annotation + Aggregation")

    data__annotate_and_aggregate = queryset_animals.annotate(
        colors_count=models.Count("colors"),
    ).aggregate(
        models.Sum("colors_count"),
        models.Avg("colors_count"),
        models.Max("colors_count"),
        models.Min("colors_count"),
    )

    logger.info(f"{data__annotate_and_aggregate=}")

    # Grouping.

    logger.info("Grouping")

    # Get the number of animals for each kind. Show "kind.name" instead of "kind_id".

    data__grouping = (
        queryset_animals.annotate(kind_name=models.F("kind__name"))
        .values("kind_name")
        .annotate(
            count=models.Count("id"),
        )
    )

    logger.info(f"{list(data__grouping)=}")

    # Get unique values for each field.

    logger.info("Get unique values for each field")

    data__unique_ages = queryset_animals.values_list("age", flat=True).order_by("age").distinct()

    logger.info(f"{list(data__unique_ages)=}")
    logger.info(f"{data__unique_ages.count()=} - {queryset_animals.count()=}")

    # Count the number of animals for each age.

    logger.info("Count the number of animals for each age")

    data__count_animals_per_age = queryset_animals.values("age").order_by("age").annotate(count=models.Count("id"))[:5]

    logger.info(f"{data__count_animals_per_age=}")

    logger.info("end")


class Command(BaseCommand):
    def handle(self, *args, **options):
        show_aggregation_info()

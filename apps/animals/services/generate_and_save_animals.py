import logging

from apps.animals.models import Animal
from apps.animals.services.generate_animals import generate_animals


def generate_and_save_animals(amount: int) -> None:
    logger = logging.getLogger("django")

    queryset = Animal.objects.all()

    logger.info(f"Current amount of animals before: {queryset.count()}")

    for animal in generate_animals(amount=amount, is_auto_generated=True):
        logger.info(f"{animal=}")

    logger.info(f"Current amount of animals after: {queryset.count()}")

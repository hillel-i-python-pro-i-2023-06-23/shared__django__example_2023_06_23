import logging

from apps.animals.models import Animal


def delete_animals(is_only_auto_generated: bool = False) -> None:
    logger = logging.getLogger("django")

    queryset = Animal.objects.all()
    logger.info(f"Current amount of animals before: {queryset.count()}")

    queryset_for_delete = queryset
    if is_only_auto_generated:
        logger.info("Delete only auto generated animals")
        queryset_for_delete = queryset_for_delete.filter(is_auto_generated=True)

    total_deleted, details = queryset_for_delete.delete()
    logger.info(f"Total deleted: {total_deleted}, details: {details}")

    logger.info(f"Current amount of animals after: {queryset.count()}")

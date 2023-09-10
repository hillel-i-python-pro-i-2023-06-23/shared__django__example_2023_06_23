from collections.abc import Iterator

from faker import Faker

from apps.animals.models import Animal, Kind, Color

faker = Faker()


def generate_animal(is_auto_generated: bool = False) -> Animal:
    animal = Animal(
        name=faker.first_name(),
        age=faker.pyint(min_value=1, max_value=47),
        is_auto_generated=is_auto_generated,
        kind=Kind.objects.order_by("?").first(),
    )

    animal.save()

    max_colors = Color.objects.count()

    while animal.colors.count() < max_colors:
        random_color_from_db = Color.objects.order_by("?").first()
        animal.colors.add(random_color_from_db)

        if faker.pybool():
            break

    return animal


def generate_animals(amount: int, is_auto_generated: bool = False) -> Iterator[Animal]:
    for _ in range(amount):
        yield generate_animal(is_auto_generated=is_auto_generated)

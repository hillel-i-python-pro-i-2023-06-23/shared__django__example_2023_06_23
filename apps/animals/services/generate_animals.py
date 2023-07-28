from collections.abc import Iterator

from faker import Faker

from apps.animals.models import Animal

faker = Faker()


def generate_animal() -> Animal:
    return Animal(
        name=faker.first_name(),
        age=faker.pyint(min_value=1, max_value=47),
    )


def generate_animals(amount: int) -> Iterator[Animal]:
    for _ in range(amount):
        yield generate_animal()

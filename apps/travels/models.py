from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__

    class Meta:
        verbose_name_plural = "Countries"


class Traveler(models.Model):
    name = models.CharField(max_length=100)

    visited_countries = models.ManyToManyField(
        Country,
        related_name="travelers",
    )

    @property
    def visited_countries_amount(self):
        return self.visited_countries.count()

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__

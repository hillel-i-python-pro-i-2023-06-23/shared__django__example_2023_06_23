from django.db import models


class Kind(models.Model):
    """
    Kind of animal.
    For example:
        - cat
        - dog
        - etc.
    """

    name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def amount_of_animals(self):
        return self.animals.count()

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__

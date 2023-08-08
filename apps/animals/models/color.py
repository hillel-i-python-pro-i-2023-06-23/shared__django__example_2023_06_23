from django.db import models


class Color(models.Model):
    """
    Color of animal.
    For example:
        - Red
        - Blue
        - etc.
    """

    value = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.value = self.value.capitalize()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__

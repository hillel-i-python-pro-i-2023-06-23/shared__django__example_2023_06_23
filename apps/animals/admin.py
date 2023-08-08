from django.contrib import admin

from apps.animals import models


# admin.site.register(models.Animal)


@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "kind",
        "is_auto_generated",
        "created_at",
        "modified_at",
    )

    list_filter = (
        "is_auto_generated",
        "created_at",
    )


@admin.register(models.Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        #
        "amount_of_animals",
        #
        "created_at",
        "modified_at",
    )


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "created_at",
        "modified_at",
    )

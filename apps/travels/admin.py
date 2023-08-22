from django.contrib import admin

from apps.travels import models


@admin.register(models.Traveler)
class HumanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "visited_countries_amount",
    )


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)

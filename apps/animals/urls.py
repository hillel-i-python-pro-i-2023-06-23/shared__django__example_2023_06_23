from django.urls import path

from . import views

app_name = "animals"

urlpatterns = [
    path("list/", views.AnimalsListView.as_view(), name="animals_list"),
]

from django.urls import path

from . import views

app_name = "animals"

urlpatterns = [
    path("list/", views.AnimalsListView.as_view(), name="animals_list"),
    #
    path("create/", views.AnimalCreateView.as_view(), name="animals_create"),
    path("update/<int:pk>/", views.AnimalUpdateView.as_view(), name="animals_update"),
    path("delete/<int:pk>/", views.AnimalDeleteView.as_view(), name="animals_delete"),
    #
    path("special-edit/<int:pk>/", views.AnimalSpecialEdit.as_view(), name="animals_special_edit"),
    #
    path("generate/", views.generate_animals_view, name="animals_generate"),
    path("delete/", views.delete_animals_view, name="animals_delete"),
]

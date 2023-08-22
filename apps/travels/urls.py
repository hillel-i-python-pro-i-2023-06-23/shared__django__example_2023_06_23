from django.urls import path

from . import views

app_name = "travels"

urlpatterns = [
    path("list/", views.TravelerListView.as_view(), name="list_of_travelers"),
]

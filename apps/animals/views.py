from django.views.generic import ListView

from apps.animals.models import Animal


class AnimalsListView(ListView):
    model = Animal

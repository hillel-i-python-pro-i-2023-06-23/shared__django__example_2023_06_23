from django.views.generic import ListView

from apps.travels import models


class TravelerListView(ListView):
    model = models.Traveler

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "List of travelers"
        context["countries"] = models.Country.objects.all()

        return context

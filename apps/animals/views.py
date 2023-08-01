from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView

from apps.animals.forms import GenerateForm, AnimalSpecialEditForm
from apps.animals.models import Animal
from apps.animals.services.delete_animals import delete_animals
from apps.animals.services.generate_and_save_animals import generate_and_save_animals


class AnimalsListView(ListView):
    model = Animal


class AnimalCreateView(CreateView):
    model = Animal
    fields = (
        "name",
        "age",
        # "is_auto_generated",
    )
    success_url = reverse_lazy("animals:animals_list")


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = (
        "name",
        "age",
        # "is_auto_generated",
    )

    def get_success_url(self):
        return reverse_lazy("animals:animals_update", kwargs=dict(pk=self.kwargs["pk"]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy("animals:animals_list")


def generate_animals_view__raw_form(request):
    if request.method == "POST":
        amount = int(request.POST["amount"])

        generate_and_save_animals(amount=amount)

    return render(
        request=request,
        template_name="animals/animals_generate__raw_form.html",
        context=dict(
            animals_list=Animal.objects.all(),
        ),
    )


def generate_animals_view(request):
    if request.method == "POST":
        form = GenerateForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data["amount"]

            generate_and_save_animals(amount=amount)
    else:
        form = GenerateForm()

    return render(
        request=request,
        template_name="animals/animals_generate.html",
        context=dict(
            animals_list=Animal.objects.all(),
            form=form,
        ),
    )


class AnimalSpecialEdit(FormView):
    model = Animal
    form_class = AnimalSpecialEditForm
    template_name = "animals/animal_form.html"

    def get_success_url(self):
        return reverse_lazy("animals:animals_special_edit", kwargs=dict(pk=self.kwargs["pk"]))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = Animal.objects.get(pk=self.kwargs["pk"])
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def delete_animals_view(request):
    delete_animals()

    return redirect(reverse_lazy("animals:animals_list"))

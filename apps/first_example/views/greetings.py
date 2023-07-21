from django.views.generic import TemplateView


# def greetings(request, name: str, age: int):
#     return render(
#         request=request,
#         template_name="first_example/greetings.html",
#         context={
#             "name": name,
#             "age": age,
#             #
#             "title": "Greetings",
#         },
#     )


class GreetingsView(TemplateView):
    template_name = "first_example/greetings.html"

    def get_context_data(self, name: str, age: int, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            name=name,
            age=age,
            #
            title="Greetings",
        )

        return context

from django.http import HttpResponse


def greetings(request, name: str, age: int):
    return HttpResponse(f"Hello, {name}! You are {age} years old!")

from django.http import HttpResponse


def index(request):
    greeting = 'Hello'
    return HttpResponse(greeting)

    
from django.shortcuts import render

# Create your views here.
# A view function takes in a request and returns a response.
# Essentially, it is a request heandler.
# So why do we call this a "view" in Django? 🫢

from django.http import HttpResponse


def say_hello(request):
    # Pull data from DB
    # Transform data
    # Send email
    return HttpResponse('Hello Taiwan!')
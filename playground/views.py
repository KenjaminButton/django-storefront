from django.shortcuts import render

# Create your views here.
# A view function takes in a request and returns a response.
# Essentially, it is a request heandler.
# So why do we call this a "view" in Django? 🫢

from django.http import HttpResponse


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Kenjamin'})

from django.urls import path
from . import views

# URLConf module aka URL Configuration module
urlpatterns = [
    # localhost:8000/playground/hello
    path('hello/', views.say_hello)
]

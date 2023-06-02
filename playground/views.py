from django.shortcuts import render
from django.db import transaction, connection
from store.models import Product, Customer, Collection, Order, OrderItem, Cart, CartItem
from tags.models import TaggedItem


def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute()

    return render(request, 'hello.html', {'name': 'Kenderson'})

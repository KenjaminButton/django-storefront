from django.db import models

# Create your models here.


class Product(models.Model):
    # Hypothetical field without ID using SKU below:
    # sku = models.CharField(max_length=10, primary_key=True)

    # Django field types
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    title = models.CharField(max_length=253)
    description = models.TextField()
    # $9999.99 maximum value or less...
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    # Automatically updates the current date time in the field
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    # Django field types
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    first_name = models.CharField(max_length=253)
    last_name = models.CharField(max_length=253)
    email = models.EmailField(max_length=253, unique=True)
    phone = models.CharField(max_length=253)
    birth_date = models.DateField(null=True)

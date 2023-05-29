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
    # Bronze, Silver, Gold membership
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    # FIXED LIST OF VALUES for uppercase
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    # Django field types
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    first_name = models.CharField(max_length=253)
    last_name = models.CharField(max_length=253)
    email = models.EmailField(max_length=253, unique=True)
    phone = models.CharField(max_length=253)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    # Pending, Complete, Failed payment
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    # FIXED LIST of values for uppercase
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    payment = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

    # The auto_now_add option sets the field value to the current date and time during object creation only, while auto_now updates the field value to the current date and time on each object save or modification.
    placed_at = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    street = models.CharField(max_length=253)
    city = models.CharField(max_length=253)

    # One to One relationship with Customer and Address
    # customer = models.OneToOneField(
    #     Customer, on_delete=models.CASCADE, primary_key=True)

    # One to Many relationship with Customer to Address
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)

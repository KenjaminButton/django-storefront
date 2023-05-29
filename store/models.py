from django.db import models

# Define Many to Many relationships between Promotion and Product


class Promotion(models.Model):
    description = models.CharField(max_length=253)
    discount = models.FloatField()
    # products

# ONE TO MANY FIELDS
# Collection - Product
# Customer - Order
# Order - Item
# Cart - Item


class Collection(models.Model):
    title = models.CharField(max_length=253)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Product(models.Model):
    # Hypothetical field without ID using SKU below:
    # sku = models.CharField(max_length=10, primary_key=True)

    # Django field types
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    title = models.CharField(max_length=253)
    description = models.TextField()
    # $9999.99 maximum value or less...
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    # Automatically updates the current date time in the field
    last_update = models.DateTimeField(auto_now=True)
    # One to Many relationship between Collection and Product
    collection = models.ForeignKey(
        # PROTECT so if we delete a collection, we don't accidently delete ALL the products in that collection
        Collection, on_delete=models.PROTECT
    )
    promotions = models.ManyToManyField(Promotion)


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

    # One to Many relationship between Customer and Order
    customer = models.ForeignKey(
        # If we delete a customer, we don't accidentally delete an order
        # String type 'Customer' because Customer class is defined AFTER Order class and I'm too lazy to move my classes around.
        'Customer', on_delete=models.PROTECT
    )


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


class Address(models.Model):
    street = models.CharField(max_length=253)
    city = models.CharField(max_length=253)

    # One to One relationship with Customer and Address
    # customer = models.OneToOneField(
    #     Customer, on_delete=models.CASCADE, primary_key=True)

    # One to Many relationship with Customer to Address
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    # One to Many relationship between Cart and Item
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

from django.contrib import admin
from store.models import Product
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from tags.models import TaggedItem
# Register your models here.


class TagInline(GenericTabularInline):
    """
    Creating an inline class for managing a tag
    """
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


"""
We have a new product admin so we need to unregister
the old one and register the new one.
"""
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=253)


class TaggedItem(models.Model):
    # What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Poor Form Implementation
    # Need to import that Product class making Tags app dependent on Store app
    # product = models.ForeignKey(Product)

    # GENERIC IMPLEMENTATION
    # Type (product, video, article)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID (limitation is primary key must be positive integer)
    object_id = models.PositiveIntegerField()
    # When querying data, getting actual object this product is applied to
    content_object = GenericForeignKey()

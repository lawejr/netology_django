from django.db import models
from django_extensions.db.fields import AutoSlugField


class Phone(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')

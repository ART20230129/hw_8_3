from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.CharField(max_length=50)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)


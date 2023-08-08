from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

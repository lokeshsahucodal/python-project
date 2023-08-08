from django.test import TestCase
from django.template.defaultfilters import slugify
from .models import Product


class ModelsTestCase(TestCase):
    def test_create_product(self):
        name = "Test Product"
        post, created = Product.objects.get_or_create(name=name, slug=slugify(name), image='https://st4.depositphotos.com/14431644/37827/i/450/depositphotos_378271014-stock-photo-word-writing-text-product-test.jpg')
        self.assertEqual(post.slug, slugify(name))

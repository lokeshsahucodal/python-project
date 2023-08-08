from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image', 'created_at']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)

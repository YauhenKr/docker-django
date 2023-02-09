from django.contrib import admin

from .models import Product, ProductAmount, Sale

admin.site.register(Product)
admin.site.register(ProductAmount)
admin.site.register(Sale)

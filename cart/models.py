from django.db import models
from django.conf import settings
from django.urls import reverse

from products.models import Product


class Cart(models.Model):
    NEW = "new"
    OLD = "old"

    STATUSES = (
        (NEW, "New cart"),
        (OLD, "Old cart"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(Product, through='CartItem')

    status = models.CharField(
        max_length=10, choices=STATUSES, default=NEW)

    def __str__(self):
        return str(self.id)

    objects = models.Manager()


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
        return f'{self.cart.id} | {self.product.name} | {self.quantity}'

    def get_absolute_url(self):
        return reverse('cart-items-retrieve-update-delete', kwargs={'id': self.id})

    objects = models.Manager()


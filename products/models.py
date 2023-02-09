from django.db import models

from categories.models import Category, Subcategory
from .services import calculate_price_with_sales


class Sale(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    percent = models.IntegerField()

    class Meta:
        ordering = ('name', 'percent')
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return self.name

    objects = models.Manager()


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', on_delete=models.CASCADE)
    code = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_with_sales = models.DecimalField(max_digits=10, decimal_places=2,
                                           null=True, blank=True)
    sales = models.ManyToManyField(Sale,
                                   related_name='sales',
                                   blank=True
                                   )
    img = models.ImageField(upload_to='product_img')
    product_details = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_available_sales(self):
        return {sale.name: sale.percent for sale in self.sales.all()}

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.price_with_sales = calculate_price_with_sales(self)
        super(Product, self).save()

    objects = models.Manager()


class ProductAmount(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.product_id} - {self.amount}'

    objects = models.Manager()


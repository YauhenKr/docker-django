from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    objects = models.Manager()


class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return f'{self.name}'

    objects = models.Manager()


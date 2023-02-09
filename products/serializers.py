from rest_framework import serializers

from products.models import (Category, Product, Sale)
from products.services import calculate_price_with_sales


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    sales = serializers.DictField(source='get_available_sales')
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'category',
            'total_price', 'sales', 'code',
            ]
        read_only_fields = ('price', )

    def get_total_price(self, obj):
        return calculate_price_with_sales(product=obj)


class ProductCreateSerializer(serializers.ModelSerializer):
    """
        Using in CartItemCreateSerializer for adding
        product in cart
    """
    class Meta:
        model = Product
        fields = ['name', 'code']




from rest_framework import serializers

from cart.models import CartItem, Cart
from products.serializers import ProductsListSerializer, ProductCreateSerializer


class CartItemCreateSerializer(serializers.ModelSerializer):
    product = ProductCreateSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CartItemDetailSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

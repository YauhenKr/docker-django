from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from rest_framework import status

from products.models import Product
from cart.models import CartItem
from .selectors import _get_cart_by_user, _get_all_cart_items_for_cart
from products.selectors import check_product_amount


def create_new_cart_item_for_user(self, request, *args, **kwargs) -> status:
    try:
        cart = _get_cart_by_user(self.request.user)
        items = _get_all_cart_items_for_cart(cart=cart)
        code = request.data['code']
        quantity = request.data['quantity']
        product = Product.objects.get(code=code)
        product_id = Product.objects.values_list('id', 'name').filter(code=code)[0][0]
        if check_product_amount(product_id):
            with transaction.atomic():
                CartItem.objects.create(cart=cart, product=product, quantity=quantity)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_204_NO_CONTENT
    except (ObjectDoesNotExist, IntegrityError):
        return status.HTTP_400_BAD_REQUEST

from .models import CartItem, Cart
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


def _get_cart_by_user(user: User) -> QuerySet[Cart]:
    """
       input: User,
       Output: Cart,
       Get Cart for current user
    """
    return Cart.objects.get(user=user, status='new')


def _get_all_cart_items_for_cart(cart) -> QuerySet[CartItem]:
    """
       input: Cart,
       Output: CartItem queryset,
       Get all CartItems for current users cart
    """
    return CartItem.objects.select_related('product').filter(cart=cart)


def get_cart_items_by_user(user: User) -> QuerySet[CartItem]:
    """
       input: User,
       Output: CartItem queryset,
       Get all CartItems for current user
    """
    cart = _get_cart_by_user(user)
    cart_items = _get_all_cart_items_for_cart(cart)
    return cart_items

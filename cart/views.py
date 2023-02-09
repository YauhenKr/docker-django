from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import CartItemsSerializer, CartItemDetailSerializer, CartItemCreateSerializer
from cart.selectors import get_cart_items_by_user
from cart.services import create_new_cart_item_for_user


@permission_classes([IsAuthenticated])
class CartItemsListCreateApi(ListCreateAPIView):

    def get_queryset(self):
        user = self.request.user
        return get_cart_items_by_user(user)

    def post(self, request, *args, **kwargs):
        status_code = create_new_cart_item_for_user(self, request, *args, **kwargs)
        return Response(status=status_code)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if hasattr(self.request, 'method'):
            if self.request.method == 'GET':
                return CartItemsSerializer
            if self.request.method == 'POST':
                return CartItemCreateSerializer


@permission_classes([IsAuthenticated])
class CartItemsRetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return get_cart_items_by_user(user)

    def update(self, request, *args, **kwargs):
        try:
            cart_item = self.get_object()
            quantity = int(request.data['quantity'])
            cart_item.quantity = quantity
            cart_item.save()
            return Response(status=status.HTTP_302_FOUND)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

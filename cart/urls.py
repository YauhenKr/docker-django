from django.urls import path

from .views import CartItemsListCreateApi, CartItemsRetrieveUpdateDestroyApi

urlpatterns = [
    path('', CartItemsListCreateApi.as_view(), name='cart-items-list'),
    path('<int:id>/', CartItemsRetrieveUpdateDestroyApi.as_view(),
         name='cart-items-retrieve-update-delete'),
]

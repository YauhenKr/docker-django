from django.urls import path, include
from .views import ProductListApiView

urlpatterns = [
    path('all/', ProductListApiView.as_view(), name='product-list'),
]

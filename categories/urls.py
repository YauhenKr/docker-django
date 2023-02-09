from django.urls import path

from categories.views import ListCategoryAPIView

urlpatterns = [
    path('all/', ListCategoryAPIView.as_view(), name='category-list'),
]

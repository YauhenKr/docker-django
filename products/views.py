from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductsListSerializer


class ProductListApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response(
            ProductsListSerializer(products, many=True).data,
            status=status.HTTP_200_OK
        )

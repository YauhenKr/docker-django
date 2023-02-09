from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from categories.models import Category
from categories.serializers import CategorySerializer


class ListCategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return Response(
            CategorySerializer(categories, many=True).data,
            status=status.HTTP_200_OK
        )



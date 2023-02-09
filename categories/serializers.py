from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from categories.models import Category, Subcategory


class CategorySerializer(ModelSerializer):
    subcategory = serializers.SerializerMethodField('get_subcategories')

    class Meta:
        model = Category
        fields = [
            'name',
            'subcategory'
        ]

    def get_subcategories(self, obj):
        return SubcategorySerializer(obj.category.all(), many=True).data


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = [
            'name',
        ]

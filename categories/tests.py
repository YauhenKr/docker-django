from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from categories.models import Category, Subcategory
from categories.serializers import CategorySerializer


class CategoryTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='name')

    def test_category_list_api(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='name')
        self.subcategory = Subcategory.objects.create(
            name='name',
            category_id=self.category
        )

    def test_category_serializer(self):
        data = CategorySerializer(instance=self.category).data
        expected_data = {
            'name': self.category.name,
            'subcategory': CategorySerializer.get_subcategories(
                self.category, self.subcategory.category_id
            )
        }
        self.assertEqual(expected_data, data)

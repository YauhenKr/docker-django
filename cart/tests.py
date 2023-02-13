from collections import OrderedDict

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from cart.selectors import get_cart_items_by_user, _get_all_cart_items_for_cart, _get_cart_by_user
from user.models import NewUser
from categories.models import Category, Subcategory
from products.models import Product, Sale, ProductAmount
from cart.models import Cart, CartItem
from cart.serializers import CartItemCreateSerializer


class CartViewsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = NewUser.objects.create(
                                        username='username',
                                        password='password',
                                        email='farw@gmail.com',
                                        first_name='John',
                                        last_name='John'
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='name')
        self.subcategory = Subcategory.objects.create(name='name', category_id=self.category)
        self.sale = Sale.objects.create(name='name',
                                        description='name',
                                        percent=10)
        self.product = Product.objects.create(
                                        name='name',
                                        price=1000,
                                        category=self.category,
                                        subcategory=self.subcategory,
                                        code=128458
        )
        self.product_amount = ProductAmount.objects.create(
                                        product_id=self.product,
                                        amount=2
        )
        self.cart = Cart.objects.get(user=self.user, status='new')

    def test_cart_items_list_api(self):
        response = self.client.get(reverse('cart-items-list'))
        self.assertEqual(response.status_code, 200)

    def test_cart_items_create_with_existing_product_api(self):
        self.data = {
            "code": 128458,
            "quantity": 1,
        }
        response = self.client.post(reverse('cart-items-list'), data=self.data)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(response.status_code, 201)


class CartSerializerTest(TestCase):
    def setUp(self):
        self.user = NewUser.objects.create(username='username', password='password')
        self.category = Category.objects.create(name='name')
        self.subcategory = Subcategory.objects.create(name='name', category_id=self.category)
        self.product = Product.objects.create(name='name',
                                              price=1000,
                                              category=self.category,
                                              subcategory=self.subcategory,
                                              code=128458
                                              )
        self.cart = Cart.objects.get(user=self.user)
        CartItem.objects.create(cart=self.cart,
                                product=self.product,
                                quantity=1,
                                )
        self.cart_item = CartItem.objects.get(cart=self.cart)

    def test_cart_item_create_serializer(self):
        data = CartItemCreateSerializer(instance=self.cart_item).data
        expected_data = {'product': OrderedDict([('name', 'name'), ('code', 128458)]),
                         'quantity': 1,
                         }
        self.assertEqual(expected_data, data)


class CartSelectorsTest(TestCase):
    def setUp(self):
        self.user = NewUser.objects.create(username='username', password='password')
        self.user_2 = NewUser.objects.create(username='username2', password='password2')
        self.category = Category.objects.create(name='name')
        self.subcategory = Subcategory.objects.create(name='name', category_id=self.category)
        self.product = Product.objects.create(name='name',
                                              price=1000,
                                              category=self.category,
                                              subcategory=self.subcategory,
                                              code=128458
                                              )
        self.cart = Cart.objects.get(user=self.user)
        CartItem.objects.create(cart=self.cart,
                                product=self.product,
                                quantity=1,
                                )
        self.cart_items = CartItem.objects.filter(cart=self.cart)
        self.empty_cart = Cart.objects.create(user=self.user_2)

    def test_get_all_cart_items_for_not_empty_cart(self):
        self.assertEqual(list(_get_all_cart_items_for_cart(self.cart)),
                         list(self.cart_items))

    def test_get_all_cart_items_for_empty_cart(self):
        self.assertEqual(
            list(_get_all_cart_items_for_cart(self.empty_cart)), [])

    def test_get_cart_by_user(self):
        self.assertEqual(_get_cart_by_user(self.user), self.cart)

    def test_get_cart_items_by_user(self):
        self.assertEqual(list(get_cart_items_by_user(self.user)),
                         list(self.cart_items))

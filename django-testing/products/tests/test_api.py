from rest_framework.test import APITestCase
from products.models import Product
from django.urls import reverse
from rest_framework import status
from decimal import Decimal
from django.contrib.auth import get_user_model

class TestProductAPI(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='testuser',
            password='testpass123'
        )

        self.client.force_authenticate(user=self.user)

    def test_get_products(self):
        Product.objects.create(name='Mouse',price=321.11,stock_count=66)
        Product.objects.create(name='keyboard',price=811,stock_count=8)

        response=self.client.get(reverse('products-api'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[0]['name'],'Mouse')
        self.assertEqual(response.data[0]['price'],'321.11')
        self.assertEqual(response.data[1]['price'],'811.00')


    def test_create_product(self):
        payload={
            'name':'monitor',
            'price':500,
            'stock_count':2,
        }
        response=self.client.post(reverse('products-api'),payload,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(len(response.data),5)
        self.assertEqual(response.data['name'], 'monitor')
        self.assertEqual(response.data['price'], '500.00')
        self.assertEqual(response.data['stock_count'], 2)
        self.assertEqual(Product.objects.get().name,'monitor')

    def test_create_invalid_product(self):
        payload={
            'name':'monitor',
            'price':-500,
            'stock_count':2,
        }
        response=self.client.post(reverse('products-api'),payload,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(),0)
        self.assertIn('price', response.data)


    def test_put_product(self):
        product=Product.objects.create(name='random',price=111,stock_count=80)
        url=reverse('product-detail',args=[product.pk])
        payload={
            'name':'playstation',
            'price':5500,
            'stock_count':20,
        }
        response=self.client.put(url,payload,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name,'playstation')
        self.assertEqual(Product.objects.get().price,Decimal('5500.00'))


    def test_patch_product(self):
        product=Product.objects.create(name='random',price=111,stock_count=80)
        updated_data={'name':'PC'}
        response=self.client.patch(reverse('product-detail',args=[product.pk]),updated_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(pk=product.pk).name,'PC')
        self.assertEqual(Product.objects.get(pk=product.pk).price,Decimal('111.00'))


    def test_delete_product(self):
        product=Product.objects.create(name='random',price=111,stock_count=80)
        response=self.client.delete(reverse('product-detail',args=[product.pk]))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(),0)


    def test_anonymous_user_cannot_get_products(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('products-api'))
        self.assertIn(response.status_code, [401, 403])


    def test_anonymous_user_cannot_create_product(self):
        self.client.force_authenticate(user=None)
        payload = {
            'name': 'Monitor',
            'price': '500.00',
            'stock_count': 10
        }

        response = self.client.post(
            reverse('products-api'),
            payload,
            format='json'
        )

        self.assertIn(response.status_code, [401, 403])
        self.assertEqual(Product.objects.count(), 0)


    def test_authenticated_user_can_get_products(self):
        Product.objects.create(
            name='Mouse',
            price=500,
            stock_count=10
        )

        response = self.client.get(reverse('products-api'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_non_admin_cant_get(self):
        self.user.is_staff=False
        self.user.is_superuser=False
        self.user.save()
        response=self.client.get(reverse('products-api'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
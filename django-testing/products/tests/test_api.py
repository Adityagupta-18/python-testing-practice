from rest_framework.test import APITestCase
from products.models import Product
from django.urls import reverse
from rest_framework import status
from decimal import Decimal

class TestProductAPI(APITestCase):

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
        

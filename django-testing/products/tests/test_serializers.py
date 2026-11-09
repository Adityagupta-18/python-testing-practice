from decimal import Decimal
from django.test import TestCase
from products.models import Product
from products.serializers import ProductSerializer


class TestProductSerializer(TestCase):

    def test_product_serializer(self):
        product=Product.objects.create(name='electronics',price=456.32,stock_count=55)
        serializer=ProductSerializer(product)
        self.assertEqual(serializer.data['name'],'electronics')
        self.assertEqual(serializer.data['price'],'456.32')
        self.assertTrue(serializer.data['in_stock'])

    def test_valid_product_data(self):
        payload = {
            'name': 'Laptop',
            'price': '500.00',
            'stock_count': 10
        }
        serializer=ProductSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'],'Laptop')
        self.assertEqual(serializer.validated_data['price'],Decimal('500.00'))

    def test_invalid_product_data(self):
        payload = {
            'name': 'Laptop',
            'price': '-500.00',
            'stock_count': 10
        }
        serializer=ProductSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

    def test_invalid_stock(self):
        payload={
            'name': 'Laptop',
            'price': '2500.00',
            'stock_count': -10
        }
        serial=ProductSerializer(data=payload)
        self.assertFalse(serial.is_valid())
        self.assertIn('stock_count',serial.errors)

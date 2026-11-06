from django.test import TestCase
from products.models import Product
from django.core.exceptions import ValidationError

class ProductmodelTest(TestCase):
    def setUp(self):
        self.product=Product(name='Testproduct',price=1000.00,stock_count=20)

    def test_in_stock(self):
        self.assertTrue(self.product.in_stock)

        self.product.stock_count=-6
        self.assertFalse(self.product.in_stock)

    def test_discount(self):
        self.assertEqual(self.product.get_discounted_price(50),500)

    def test_negative_price(self):
        self.product.price=-45
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_Stock(self):
        self.product.stock_count=-5
        with self.assertRaises(ValidationError):
            self.product.clean()
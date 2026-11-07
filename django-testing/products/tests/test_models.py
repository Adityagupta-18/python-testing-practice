from django.test import TestCase
from products.models import Product
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class ProductmodelTest(TestCase):

    # run for every test and then tear down
    # def setUp(self):
    #     self.product=Product(name='Testproduct',price=1000.00,stock_count=20)

    @classmethod
    def setUpTestData(cls):
        cls.product=Product(name='test_data',price=1000,stock_count=45)

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

    def test_negprice_contraint(self):
        product=Product(name='negative_price',price=-4215,stock_count=44)
        with self.assertRaises(IntegrityError):
            product.save()

    def test_negstock_constraint(self):
        product=Product(name='neg_stock',price=45645,stock_count=0)
        with self.assertRaises(IntegrityError):
            product.save()
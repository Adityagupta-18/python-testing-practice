from django.test import TestCase, SimpleTestCase
from products.models import Product
from django.urls import reverse

class testHomePage(SimpleTestCase):

    def test_home_status_code(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_home_template(self):
        resp=self.client.get('/')
        self.assertTemplateUsed(resp,'index.html')

    def test_page_content(self):
        resp=self.client.get('/')
        self.assertContains(resp,'page')


class TestProdcutPage(TestCase):
    def setUp(self):
        Product.objects.create(name='electronics',price=7645.74,stock_count=456)
        Product.objects.create(name='crockery',price=745.74,stock_count=46)

    def test_product_template(self):
        response=self.client.get(reverse('products'))
        self.assertTemplateUsed(response,'products.html')

    def test_product_context(self):
        response=self.client.get(reverse('products'))
        self.assertContains(response,'crockery')
        self.assertEqual(len(response.context['products']),2)

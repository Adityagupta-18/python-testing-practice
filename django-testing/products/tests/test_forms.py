from django.test import TestCase
from products.models import Product
from django.urls import reverse

class TestProductForm(TestCase):

    def test_valid_form(self):
        sample_prod={
            'name':'form_sample',
            'price':5546,
            'stock_count':55
        }
        response=self.client.post(reverse('products'),data=sample_prod)
        self.assertEqual(response.status_code,302)
        self.assertTrue(Product.objects.filter(name='form_sample').exists())

    def test_invalid_form(self):
        invalid_sample={
            'name':'wrong',
            'price':-5465,
            'stock_count':-54
        }
        response=self.client.post(reverse('products'),data=invalid_sample)
        self.assertEqual(response.status_code,200)
        self.assertTrue("form" in response.context)
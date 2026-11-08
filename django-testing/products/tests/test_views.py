from django.test import TestCase, SimpleTestCase
from products.models import Product, User
from django.urls import reverse


class TestAuth(TestCase):

    def test_unauth_user(self):
        resp=self.client.get(reverse('profile'))
        self.assertRedirects(resp,expected_url=f"{reverse('login')}?next={reverse('profile')}")

    def test_profile_auth(self):
        User.objects.create_user(username='testuser',password='pass123')
        self.client.login(username='testuser',password='pass123')

        response=self.client.get(reverse('profile'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'testuser')



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

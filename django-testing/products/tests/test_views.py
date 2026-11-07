from django.test import TestCase, SimpleTestCase


class testHomePage(SimpleTestCase):

    def test_home_status_code(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_home_template(self):
        resp=self.client.get('/')
        self.assertTemplateUsed(resp,'index.html')

    def test_page_content(self):
        resp=self.client.get('/')
        self.assertContains(resp,'Welcome')
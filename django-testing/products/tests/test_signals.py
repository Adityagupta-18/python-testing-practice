from django.test import TestCase
from unittest.mock import patch
from products.models import User

class TestWelcomeSignal(TestCase):

    @patch('products.signals.send_mail')
    def test_welcome_email(self,mock_mail):
        User.objects.create_user(username='testuser',email='test@gmail.com',password='pass1234')
        mock_mail.assert_called_once_with(
            'This is a sample mail subject',
            'mail content', 
            'admin@django.com', 
            ['test@gmail.com'], 
            fail_silently=False,
        )

    @patch('products.signals.send_mail')
    def test_not_email_update(self,mock_mail):
        user=User.objects.create(username='testuser',email='test@gmail.com',password='pass1234')
        mock_mail.reset_mock()
        user.email='thisisnew@gmail.com'
        user.save()

        mock_mail.assert_not_called()
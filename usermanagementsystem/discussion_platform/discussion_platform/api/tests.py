from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTests(APITestCase):

    def test_create_user(self):
        url = reverse('create-user')
        data = {'username': 'testuser', 'password': 'testpass', 'mobile_no': '1234567890', 'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        user = User.objects.create_user(username='testuser', password='testpass', mobile_no='1234567890', email='test@example.com')
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

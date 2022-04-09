
import email
from rest_framework.test import APITestCase, force_authenticate, APIClient
from .models import User
from django.urls import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework import status
from django.urls import reverse

class ClientTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='sunnat713', password='123123asdasd', email='sunnat@sunnat.com')
        # User.objects.create(username="ifuitu", password="123456", email="ifuitu@gmail.com")
        self.username="ifuitu"
        self.password="123456"
        self.email="ifuitu@gmail.com"
        self.confirm = "123456"
        self.phone = '+99899670804'

    def test_user(self):
        response_login = self.client.post("http://127.0.0.1:8000/uz/client/Login/",
                                    {'username': 'sunnat713', 'password': '123123asdasd'},
                                    format='json')
        self.assertEqual(response_login.status_code, 200)

        response_register = self.client.post("http://127.0.0.1:8000/uz/client/register/", {
            'username': self.username,
            'phone': self.phone,
            'email': self.email,
            'password': self.password,
            'confirm': self.confirm
        }, format='json')
        self.assertEquals(response_register.status_code, status.HTTP_201_CREATED)
        
        token = response_login.data["token"]
        header = {"HTTP_AUTHORIZATION":"Token " + token}    
        
        response_me = self.client.get("http://127.0.0.1:8000/uz/client/me/{}/".format(response_login.data['user']['id']),
                                {}, **header,
                                format='json')
        self.assertEqual(response_me.status_code, 200)
    
        response_logout = self.client.delete('http://127.0.0.1:8000/ru/client/Logout/', {},
                                    **header, format='json')
        self.assertEqual(response_logout.status_code, 200)
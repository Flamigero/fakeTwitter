""" Users  Tests """

# Python
import unittest

# Django
from django.test import TestCase

# Models
from users.models import User, Profile

class UserTest(TestCase):

    def test_login_requests(self):
        # Login get
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

        # Login post
        response = self.client.post('/users/login/', {'email': 'testing@testing.com', 'password': 'testing'})
        self.assertEqual(response.status_code, 200)

    def test_signup_requests(self):
        # Singup get
        response = self.client.get('/users/signUp/')
        self.assertEqual(response.status_code, 200)

        # Signup post
        reponse = self.client.post('/users/signUp/', {'username': 'test', 'email': 'test@test.com', 
                                                      'phone': 654789123, 'password': 'testpassword', 'rePassword': 'testpassword'})
        self.assertEqual(response.status_code, 200)
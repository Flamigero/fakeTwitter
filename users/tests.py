""" Users  Tests """

# Django
from django.test import TestCase

# Models
from users.models import User, Profile

class UserModelsTest(TestCase):
    def setUp(self):
        self.username = 'test'
        self.email = 'test@test.com'
        self.phone_number = '654789123'
        self.password = 'test'

        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            phone_number=self.phone_number,
            password=self.password
        )
        self.profile = Profile.objects.create(user=self.user)
        self.profile.save()

    def test_user_create(self):
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.phone_number, self.phone_number)

    def test_user_update(self):
        firstName = 'test'
        lastName = 'test'
        phone_number = '123456789'
        self.user.first_name = firstName
        self.user.last_name = lastName
        self.user.phone_number = phone_number
        self.user.save()

        self.assertEqual(self.user.first_name, firstName)
        self.assertEqual(self.user.last_name, lastName)
        self.assertEqual(self.user.phone_number, phone_number)

    def test_profile_update(self):
        description = 'Test description'
        authenticated = True
        self.profile.description = description
        self.profile.is_authenticated = authenticated
        self.profile.save()

        self.assertEqual(self.profile.description, description)
        self.assertEqual(self.profile.is_authenticated, authenticated)

    def test_user_has_profile(self):
        userPk = self.user.pk
        profilePk = self.profile.user.pk
        self.assertEqual(userPk, profilePk)

class UserViewsTest(TestCase):

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
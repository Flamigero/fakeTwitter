""" Messages tests """

# Django
from django.test import TestCase

# Models
from messages.models import Message
from users.models import User, Profile

class MessageModelsTest(TestCase):
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

    def test_message_create(self):
        text = 'Test message'
        message = Message.objects.create(text=text, user=self.user)
        
        self.assertEqual(message.text, text)
        self.assertEqual(message.user.pk, self.user.pk)

class MessageViewsTest(TestCase):
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
        self.message = Message.objects.create(text='Test message', user=self.user)

    def test_feed_requests(self):
        # Get
        self.client.login(email=self.email, password=self.password)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Post
        response = self.client.post('/', {'user': self.user, 'text': 'Test message'})
        self.assertEqual(response.status_code, 200)
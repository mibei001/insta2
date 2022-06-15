from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Profile, NewPost
import datetime

# Create your tests here.


class Post(TestCase):
    def setUp(self):
        self.image_name = Post(image_name='reading')
        self.image_caption = Post(image_caption='caption')
        self.username = Post(mtumiaji='kevin')
        self.timed_created = Post(timed_created='2022,01,10')

    def test_string(self):
        self.assertEqual(str(self.image_name), 'reading')

    def test_string(self):
        self.assertEqual(str(self.image_caption), 'caption')

    def test_string(self):
        self.assertEqual(str(self.username), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.timed_created), '2022,01,10')


class Comment(TestCase):
    def setUp(self):
        self.body = Post(body='text body')
        self.post = Post(post='caption')
        self.mtumiaji = Post(mtumiaji='kevin')
        self.timed_created = Post(timed_created='2022,01,10')

    def test_string(self):
        self.assertEqual(str(self.body), 'text body')

    def test_string(self):
        self.assertEqual(str(self.post), 'caption')

    def test_string(self):
        self.assertEqual(str(self.mtumiaji), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.timed_created), '2022,01,10')


class Profile(TestCase):
    def setUp(self):
        self.username = Profile(username='kevin')
        self.bio = Profile(bio='this is my bio')

    def test_string(self):
        self.assertEqual(str(self.bio), 'this is my bio')

    def test_string(self):
        self.assertEqual(str(self.username), 'kevin')

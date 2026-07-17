from django.test import TestCase
from django.contrib.auth.models import User

from post.models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="12345678"
        )

    def test_create_post(self):
        post = Post.objects.create(
            title="Django",
            content="DRF Test",
            author=self.user
        )

        self.assertEqual(post.title, "Django")
        self.assertEqual(post.content, "DRF Test")
        self.assertEqual(post.author, self.user)
        self.assertEqual(Post.objects.count(), 1)
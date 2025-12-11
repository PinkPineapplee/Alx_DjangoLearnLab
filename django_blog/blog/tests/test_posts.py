# blog/tests/test_posts.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass1234')
        self.other = User.objects.create_user(username='bob', password='pass1234')
        self.post = Post.objects.create(title='Hello', content='World', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('post-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Hello')

    def test_detail_view(self):
        resp = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'World')

    def test_create_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertNotEqual(resp.status_code, 200)  # redirects to login
        self.client.login(username='alice', password='pass1234')
        resp = self.client.post(reverse('post-create'), {'title':'New', 'content':'Text'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Post.objects.filter(title='New').exists())

    def test_update_by_author_only(self):
        self.client.login(username='bob', password='pass1234')
        resp = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertNotEqual(resp.status_code, 200)  # bob can't edit alice's post
        self.client.login(username='alice', password='pass1234')
        resp = self.client.post(reverse('post-update', kwargs={'pk': self.post.pk}), {'title':'Updated','content':'X'}, follow=True)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated')

    def test_delete_by_author_only(self):
        self.client.login(username='bob', password='pass1234')
        resp = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(Post.objects.filter(pk=self.post.pk).exists(), True)
        self.client.login(username='alice', password='pass1234')
        resp = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}), follow=True)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail
from django.contrib.auth import get_user_model

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet = Snippet.objects.create(
            title="title1",
            code="printf('hello')",
            description="description1",
        )


    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

"""
    def test_should_return_username(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.Username)
"""
from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail
from django.contrib.auth import get_user_model

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()


class SnippetDetailtest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.snippet = Snippet.objects.create(
            title="タイトル",
            code="コード",
            description="解説",
        )
    
    def test_should_use_expected_template(self):
        reponse = self.client.get('/snippet/%s/' % self.snippet.id)
        self.assertTemplateUsed(reponse, "snippets/snippet_detail.html")
        
    def test_top_page_returns_200_and_expected_heading(self):
        reponse = self.client.get('/snippet/%s/' % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)
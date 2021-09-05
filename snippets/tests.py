from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail
from django.contrib.auth import get_user_model

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()


class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.client.force_login(self.user) # ログイン
    
    
    def test_render_creation_form(self):
        response = self.client.get('/snippet/new/')
        self.assertContains(respose,  "スニペットの登録", status_code=200)
    
    
    def test_create_snippet(self):
        data = {'title': 'タイトル','code':'コード', 'description':'解説'}
        self.client.post('/snippets/new/', data)
        snippet = Snippet.objects.get(title='タイトル')
        self.assertEqual('コード', snippet.code)
        self.assertEqual('解説', snippet.description)
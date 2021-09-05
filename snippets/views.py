from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from snippets.models import Snippet

def top(request):
    snippets = Snippet.objects.all() #Snippet一覧を取得
    context = {"snippets":snippets}
    return render(request, "snippets/top.html", context)


def snippet_new(request):
    return HttpResponse('スニッペットの登録')


def snippet_edit(request, snippet_id):
    return HttpResponse('スニッペットの編集')


def snippet_detail(request, snippet_id):
    return HttpResponse('スニッペットの詳細閲覧')
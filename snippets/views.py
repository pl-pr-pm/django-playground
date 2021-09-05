from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def top(request):
    return render(request, "snippets/top.html")


def snippet_new(request):
    return HttpResponse('スニッペットの登録')


def snippet_edit(request, snippet_id):
    return HttpResponse('スニッペットの編集')


def snippet_detail(request, snippet_id):
    return HttpResponse('スニッペットの詳細閲覧')
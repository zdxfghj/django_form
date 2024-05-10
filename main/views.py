from django.shortcuts import render
from django.http import HttpResponse
from form.forms import ArticleForm


def index(request):
    form = ArticleForm()
    return render(request,'main/index.html', {'title': "Главная страница !!!", 'form': form})


def about(request):
    return render(request, 'main/about.html')
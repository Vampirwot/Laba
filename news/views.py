from django.http import Http404
from django.shortcuts import render
from news.models import News
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    allNews = News.objects.all()
    context = {
        'news': allNews,
    }
    return render(request, 'index.html', context)


def get_news(request, url):
    currentNews = get_object_or_404(News, url=url)
    context = {
        'news': currentNews,
    }
    return render(request, 'news/content.html', context)

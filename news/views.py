from django.shortcuts import render
from news.models import News


# Create your views here.
def index(request):
    allNews = News.objects.all()
    context = {
        'news': allNews,
    }
    return render(request, 'index.html', context)


def get_news(request, url):
    currentNews = News.objects.get(url=url)
    context = {
        'news': currentNews,
    }
    return render(request, 'news/content.html', context)

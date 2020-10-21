from django.shortcuts import render
from news.models import News


# Create your views here.
def index(request):
    allNews = News.objects.all()
    context = {
        'news': allNews,
    }
    return render(request, 'index.html', context)


def getNews(request, pk):
    currentNews = News.objects.get(pk=pk)
    context = {
        'news': currentNews,
    }
    return render(request, 'content.html', context)

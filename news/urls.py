
from django.contrib import admin
from django.urls import path, include, re_path
from news.views import index, get_news

urlpatterns = [
    path('', index),
    re_path(r'^(?P<url>\d+-\d+)$', get_news),
]
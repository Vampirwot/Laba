
from django.contrib import admin
from django.urls import path, include, re_path
from news.views import index, getNews

urlpatterns = [
    path('', index),
    re_path(r'^(?P<pk>\d+)$', getNews),
]
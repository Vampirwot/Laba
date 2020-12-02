
from django.contrib import admin
from django.urls import path, include, re_path
from feedback.views import create_feedback

urlpatterns = [
    path('', create_feedback)
]
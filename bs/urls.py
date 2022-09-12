#gsk/urls.py
from django.contrib import admin
from django.urls import path, include

from bs.views import bs
from gsk.views import *
from modal.views import modal

urlpatterns = [
    path('', bs, name='bs'),
]

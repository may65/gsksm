#gsk/urls.py
from django.contrib import admin
from django.urls import path, include

from gsk.views import *
from modal.views import modal

urlpatterns = [
    path('', modal, name='modal'),
]

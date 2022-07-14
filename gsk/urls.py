#gsk/urls.py
from django.contrib import admin
from django.urls import path, include

from gsk.views import *

urlpatterns = [
    path('', gsk, name='gsk'),
    path('login/', user_login, name='login'),
]

#gsk/urls.py
from django.contrib import admin
from django.urls import path, include

from gsk.views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    # path('mbr/', mbr, name='mbr'),
    # path('', gsk, name='gsk'),
    path('', mbr, name='mbr'),
]

from django.template.defaulttags import url
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # url(r'^register/$', views.register, name='register'),
    path('register/', views.register, name='register'),
]

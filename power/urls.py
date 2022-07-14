#gsk/urls.py
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import *

from gsk.views import *
from power.views import LineView

urlpatterns = [
    # path('', views.LineView.as_view, name='line'),
    path('', power, name='power'),
    path('line_list/', line_list, name='line_list'),
    path('box_list/', box_list, name='box_list'),
    path('count_line/', count_line, name='count_line'),
    path('count_box/', count_box, name='count_box'),
    # path('login/', user_login, name='login'),
]

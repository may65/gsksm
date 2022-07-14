# from django.http import request
from django.urls import path

# from . import views
# from .views import test
from .views import *

from django.conf import settings
# from django.conf.urls import include, url
from . import views

# urlpatterns = [
# 	url(r'^$', views.home, name='home'),
# ]

app_name = 'vote'
urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('', views.VotesAllView.as_view(), name='votes'),
    path('log/', views.LogAllView.as_view(), name='log'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/voteuser/', views.voteuser, name='voteuser'),
    # path('test/', testhtml, name='test'),
    # path('test/', views.IndexView.as_view(), name='index'),
    # path('test/', test),
    # path('testhtml/', testhtml),
    # path('testview/', views.TestView.as_view(), name='testview'),
    # path('index/', views.IndexView.as_view(), name='index'),
]
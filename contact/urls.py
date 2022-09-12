# /news/urls.py
from django.urls import path, include

import contact
from .views import *

# app_name = 'news'
urlpatterns = [
    # path('', include(router.urls)),
    path('', contact, name='contact'),
    # path('addpage/', addpage, name='addpage'),
    # path('newstest/', newstest, name='newstest'),
    # path('<slug:post_slug>/', one_new, name='one_new'),
]


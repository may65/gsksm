from django.urls import path

from .views import *

urlpatterns = [
    path('test/',test,name='test'),
    path('', forum, name='forum'),
    path('<int:forum_id>/', forum_id, name='forum_id'),
    path('<int:forum_id>/<int:topic_id>/', topic_id, name='topic_id'),
    # path('post/<int:forum_id>/<int:topic_id>/', post_new, name='post_new'),
]

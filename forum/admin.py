# admin
from django.contrib import admin
from .models import *

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    pass
    list_display = ('forum','desc','date')
    # list_display = list_fields(Forum)
    # list_display_links = list_display
    # search_fields = list_display

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
    list_display = ('id','topic','date','forum','user')
    # list_display = list_fields(Topic)
    # list_display_links = list_display
    # search_fields = list_display

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    list_display = ('id','post','date','user','forum','topic')
    # list_display = list_fields(Post)
    # list_display_links = list_display
    # search_fields = list_display

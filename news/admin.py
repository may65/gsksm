# admin.py

from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('author', 'time_update', 'photo', 'file', 'title')
    # list_display = list_fields(Post)

@admin.register(Now)
class NowAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("title",)}
    list_display = ('user', 'date', 'title')

# admin.site.register(Post, PostAdmin)

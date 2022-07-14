# admin.py

from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("title",)}
    # list_display = ('forum', 'desc', 'date')
    list_display = list_fields(Post)

# admin.site.register(Post, PostAdmin)

# admin
from django.contrib import admin
from .models import *

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    pass
    exclude = ('author','file') # скрыть author поле, чтобы оно не отображалось в форме изменений
    list_display = ('forum','date','desc')
    # list_display = list_fields(Forum)
    # list_display_links = list_display
    # search_fields = list_display
    # exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
    exclude = ('author','file') # скрыть author поле, чтобы оно не отображалось в форме изменений
    list_display = ('topic','forum','date','desc')
    # list_display = list_fields(Topic)
    # list_display_links = list_display
    # search_fields = list_display
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    exclude = ('author','file') # скрыть author поле, чтобы оно не отображалось в форме изменений
    list_display = ('date','body','post','topic','forum',)
    # list_display = list_fields(Post)
    # list_display_links = list_display
    # search_fields = list_display
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

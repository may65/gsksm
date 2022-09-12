from django.contrib import admin

from .models import *

# from .models import CustomUser

# admin.site.register(CustomUser)
admin.site.register(Log)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений
    # list_display = ('date','body','post','topic','forum',)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # exclude = ('author','file') # скрыть author поле, чтобы оно не отображалось в форме изменений
    # list_display = ('date','body','post','topic','forum',)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Question, QuestionAdmin)
# admin.site.register(CustomUser,CustomUserAdmin)

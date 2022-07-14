from django.contrib import admin

# Register your models here.
from power.models import *


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id','line','date')
    list_display = list_fields(Line)

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass
    # list_display = ('box',)
    list_display = list_fields(Box)

@admin.register(CountLine)
class CountLineAdmin(admin.ModelAdmin):
    pass
    # list_display = ('line','count','date')
    list_display = list_fields(CountLine)

@admin.register(CountBox)
class CountBoxAdmin(admin.ModelAdmin):
    pass
    # list_display = ('box','count','date')
    list_display = list_fields(CountBox)

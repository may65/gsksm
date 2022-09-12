from django.contrib import admin

# Register your models here.
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("title",)}
    list_display = ('top', 'date', )

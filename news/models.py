# models.py

# Create your models here.
from django.core import serializers
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse

def list_fields(Model):
    pass
    fs = serializers.serialize( "python", Model.objects.all() )
    th = fs[0]['fields'].keys()
    return tuple(th)
    # return Model._meta.get_fields()

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'название новости')
    body = models.TextField(verbose_name = 'текст новости')
    # timestamp = models.DateTimeField()
    author = models.ForeignKey(User,related_name='news_post', on_delete=models.CASCADE, verbose_name = 'автор')
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank= True)
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файл", null=True, blank= True)
    time_create = models.DateTimeField(auto_now_add=True, null=True,verbose_name = 'создан')
    time_update = models.DateField(verbose_name = 'изменен')#auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")#,null=True)
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
        # return self.body
    def __dir__(self):
        return ['title','body','author','file','time_update','slug']
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

# (self, verbose_name=None, name=None, primary_key=False,
#                  max_length=None, unique=False, blank=False, null=False,
#                  db_index=False, rel=None, default=NOT_PROVIDED, editable=True,
#                  serialize=True, unique_for_date=None, unique_for_month=None,
#                  unique_for_year=None, choices=None, help_text='', db_column=None,
#                  db_tablespace=None, auto_created=False, validators=(),
#                  error_messages=None)

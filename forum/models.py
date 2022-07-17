from django.contrib.auth.models import User
from django.core import serializers
from django.db import models

# Create your models here.

def list_fields(Model):
    pass
    fs = serializers.serialize( "python", Model.objects.all() )
    th =['id']
    th += fs[0]['fields'].keys()
    return tuple(th)

class Forum(models.Model):
    """A forum
    >>> # Create a category
    >>> c = Category.objects.create(name='a')
    >>> c.save()
    >>> # Create a forum
    >>> f = Forum.objects.create(category=c, name='a', slug='a', description='a')
    >>> f.save()
    """
    forum = models.CharField(max_length=255, verbose_name="Название форума")
    desc = models.CharField(max_length=255, verbose_name="Описание форума")
    date_create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    date = models.DateTimeField(auto_now = True,verbose_name='изменен')
    def get_url(self):
        return "/forum/%s/" % self.id
    def __str__(self):
        return self.forum
    class Meta:
        verbose_name = 'Форум'
        verbose_name_plural = 'Форумы'

class Topic(models.Model):
    topic = models.CharField(max_length=255, verbose_name="Тема")
    desc = models.CharField(max_length=255, verbose_name="Описание")
    date_create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    date = models.DateTimeField(auto_now = True, verbose_name='изменен')
    # date = models.DateTimeField(verbose_name='изменен')
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файл", null=True, blank= True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='forum_topic', on_delete=models.CASCADE)
    body = models.TextField(max_length=1024)
    def __str__(self):
        return self.topic
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

class Post(models.Model):
    post = models.CharField(max_length=255, verbose_name="Сообщение")
    desc = models.CharField(max_length=255, verbose_name="Описание",blank=True)
    date_create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    date = models.DateTimeField(auto_now = True, verbose_name='изменен')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='forum_post', on_delete=models.CASCADE)
    body = models.TextField(max_length=1024)
    def __str__(self):
        return self.post
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


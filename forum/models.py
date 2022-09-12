from django.contrib.auth.models import User
from django.core import serializers
from django.db import models

# Create your models here.

# class Reg(models.Model):
#     # user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
#     auth = models.IntegerField(default=0)
#     unauth = models.IntegerField(default=0)
#     date = models.DateTimeField(auto_now_add = True,verbose_name='дата')
#     ip = models.GenericIPAddressField(default=0)

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
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    forum = models.CharField(max_length=255, verbose_name="Форум",blank=True,null=True)
    desc = models.CharField(max_length=255, verbose_name="Описание форума", null=True, blank= True)
    create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    date = models.DateTimeField(auto_now = True,verbose_name='изменен')
    img = models.ImageField(upload_to="img/%Y/%m/%d/", verbose_name="фото", null=True, blank=True)
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файл", null=True, blank=True)
    def get_url(self):
        return "/forum/%s/" % self.id
    def __str__(self):
        return self.forum
    class Meta:
        verbose_name = 'Форум'
        verbose_name_plural = 'Форумы'

class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE,blank=True,null=True)
    topic = models.CharField(max_length=255, verbose_name="Тема",blank=True,null=True)
    desc = models.CharField(max_length=255, verbose_name="Описание темы", null=True, blank= True)
    create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    date = models.DateTimeField(auto_now = True, verbose_name='изменен')
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файл", null=True, blank= True)
    img = models.ImageField(upload_to="img/%Y/%m/%d/", verbose_name="фото", null=True, blank=True)
    def __str__(self):
        return self.topic
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE,blank=True,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,blank=True,null=True)
    post = models.CharField(max_length=255, verbose_name="Сообщение",blank=True,null=True)
    desc = models.CharField(max_length=255, verbose_name="Описание", null=True, blank= True)
    create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    date = models.DateTimeField(auto_now = True, verbose_name='изменен')
    file = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файл", null=True, blank= True)
    img = models.ImageField(upload_to="img/%Y/%m/%d/", verbose_name="фото", null=True, blank=True)
    body = models.TextField(max_length=1024, verbose_name="Текст",)
    # post = models.CharField(max_length=255, verbose_name="Сообщение")
    # desc = models.CharField(max_length=255, verbose_name="Описание",blank=True)
    # date_create = models.DateTimeField(auto_now_add = True, verbose_name="создан")
    # date = models.DateTimeField(auto_now = True, verbose_name='изменен')
    # forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # user = models.ForeignKey(User,related_name='forum_post', on_delete=models.CASCADE)
    # body = models.TextField(max_length=1024)
    def __str__(self):
        return self.body
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


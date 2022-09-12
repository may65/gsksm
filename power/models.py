from django.contrib.auth.models import User
from django.core import serializers
from django.db import models

# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=150, verbose_name = 'посты')
#     body = models.TextField()
#     # timestamp = models.DateTimeField()
#     author = models.ForeignKey(User,related_name='news_post', on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank= True)
#     time_create = models.DateTimeField(auto_now_add=True, null=True)
#     time_update = models.DateTimeField(auto_now=True, null=True)
#     # is_published = models.BooleanField(default=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",null=True)
#     def __str__(self):
#         return self.title
from django.urls import reverse

class Power(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'название новости')
    body = models.TextField(verbose_name = 'текст новости')
    # timestamp = models.DateTimeField()
    author = models.ForeignKey(User,related_name='power_post', on_delete=models.CASCADE, verbose_name = 'автор')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank= True)
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

def list_fields(Model):
    pass
    fs = serializers.serialize( "python", Model.objects.all() )
    # th =['id']
    # th =[]
    th = fs[0]['fields'].keys()
    return tuple(th)

class Line(models.Model):
    pass
    line = models.CharField(max_length=16)
    date = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.line
    class Meta:
        verbose_name = 'Ряд'
        verbose_name_plural = 'Ряды'

class Box(models.Model):
    pass
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    box = models.CharField(max_length=16)
    date = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.box
    class Meta:
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'

class CountLine(models.Model):
    pass
    line = models.ForeignKey(Line, on_delete=models.CASCADE,verbose_name='ряд')
    count = models.FloatField(default=0,verbose_name='счетчик')
    date = models.DateField(verbose_name='дата')
    def __str__(self):
        return str(self.line)
    class Meta:
        verbose_name = 'Счет ряда'
        verbose_name_plural = 'Счет рядов'

class CountBox(models.Model):
    pass
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    box = models.CharField(max_length=16)
    count = models.FloatField(default=0)
    date = models.DateField()
    def __str__(self):
        return self.box
    class Meta:
        verbose_name = 'Счет бокса'
        verbose_name_plural = 'Счет боксов'


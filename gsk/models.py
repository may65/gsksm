from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class Viewer(models.Model):
#     # user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
#     auth = models.IntegerField(default=0)
#     unauth = models.IntegerField(default=0)
#     date = models.DateTimeField(auto_now_add = True,verbose_name='дата')
#     ip = models.GenericIPAddressField(default=0)

class Views(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    username = models.CharField(max_length=255, verbose_name="пользователь")
    auth = models.IntegerField(default=0)
    noauth = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add = True,verbose_name='дата')
    ip = models.GenericIPAddressField(default=0)

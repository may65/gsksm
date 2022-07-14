import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=6)
    def __str__(self):
        return self.user.username

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User was created successfully.")
        else:
            return HttpResponse("There was an error.")
    else:
        form = UserForm()

    return render (request, 'home.html', {'form': form})

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    date_vote = models.DateTimeField(auto_now=True)
    # author = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'

class Log(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # votes = models.IntegerField(default=0)
    date_vote = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

class Testhtml(models.Model):
    numb = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)


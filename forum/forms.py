from django import forms
from .models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PostForm(forms.ModelForm):
    # your_name = forms.CharField(label='Your name', max_length=100)
    body = forms.CharField(label='Ваше сообщение',max_length=1024,widget=forms.Textarea(attrs={ 'rows': 2}))#'cols': 80,
    class Meta:
        model = Post
        fields = ('body',)

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()#widget=forms.PasswordInput)
    password = forms.CharField()#widget=forms.PasswordInput)
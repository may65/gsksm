from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name')#, 'email')
        labels = {
            'username': 'Login',
            'first_name': 'ФИО',
            'password1': 'My Password1 Label',
            'password2': 'My Password2 Label',
        }
        help_texts = {
            # 'username': 'My username help_text',
            'username': '',
            'password1': 'My password1 help_text',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
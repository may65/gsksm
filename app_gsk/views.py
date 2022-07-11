from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.

def menuitem():
    menu = {'/app_gsk/':'ГСК','/news/':'Новости','/forum/':'Форум','/vote/':'Опрос','/l5/':'Электричество','link6':''}
    return menu

def gsk(request):
    gsk='app_gsk text'
    menu = menuitem()
    # return HttpResponse('hello world')
    return render(request,'app_gsk/gsk.html', {'menu':menu,'app_gsk':gsk})#,{'td':td,'th':th})
    # return render(request,'base.html', {'app_gsk':app_gsk})#,{'td':td,'th':th})



def user_login(request):
    menu = '123'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    # return render(request, 'account/login.html', {'form': form})
    return render(request, 'registration/login.html', {'menu':menuitem(),'form': form})

from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.
# from .models import Viewer, Views
from .models import Views


def menuitem():
    menu = {'/gsk/':'ГСК','/news/':'Новости','/forum/':'Форум','/vote/':'Опрос','/l5/':'Электричество','link6':''}
    return menu

def mbr(request):
    views = Views()
    if request.user.is_authenticated:
        views.auth += 1
        views.user = request.user
        views.username = request.user.username
        count = Views.objects.aggregate(Sum("auth"))
        pass
    else:
        views.noauth += 1
        count = Views.objects.aggregate(Sum("noauth"))
        pass
    views.ip = request.META.get('REMOTE_ADDR')
    views.save()
    return render(request,'mbr_base.html',{'count':count,})#,{'td':td,'th':th})#, {'menu':menu,'gsk':gsk})#,{'td':td,'th':th})
    # return HttpResponse('mbr')

def gsk(request):
    gsk='gsk text'
    menu = menuitem()
    # viewer = Viewer()
    # if not request.user.is_authenticated():
    #     pass
    #     viewer.user = request.user
    # else:
    #     pass
    #     viewer.user = 'anonymous'
    # return HttpResponse('hello world')
    return render(request,'gsk/gsk.html', {'menu':menu,'gsk':gsk})#,{'td':td,'th':th})
    # return render(request,'base.html', {'gsk':gsk})#,{'td':td,'th':th})



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
                    # return HttpResponse('Authenticated successfully')
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    # return render(request, 'account/login.html', {'form': form})
    return render(request, 'registration/login.html', {'menu':menuitem(),'form': form})

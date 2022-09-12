# views.py

from django.template import RequestContext
#############
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
# ]

def news(request):
    ''' Show all news '''
    # print(123)
    # cities = [{'id': 1, 'city': 'Москва'},
    #           {'id': 5, 'city': 'Тверь'},
    #           {'id': 7, 'city': 'Минск'},
    #           {'id': 8, 'city': 'Смоленск'},
    #           {'id': 11, 'city': 'Калуга'}]
    posts = Post.objects.all().order_by('-time_update')
    nows = Now.objects.all().order_by('date')
    # fields = list_fields(Post)
    # field = dir(Post())
    # t = type(field)
    return render(request, 'news/news.html', {'posts':posts,'nows':nows,})
    #'fields':fields,'field':field,'t':t})#,'cities':cities})

# после функции news дописать
# def one_new(request, post_id):
def one_new(request, post_slug):
    ''' Show single news'''
    # post = get_object_or_404(Post, pk=post_id)
    post = get_object_or_404(Post, slug=post_slug)
    vars = dict(
        title=post.title,
        body=post.body,
        author=post.author,
        # photo=post.photo,
        file=post.file,
        photo=post.photo,
        time_update=post.time_update,
        slug=post_slug,
    )
    return render(request,'news/one_new.html', vars)#, context_instance=RequestContext(request))

def newstest(request):
    print(123)
    pass
    return HttpResponse('newstest')

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('news:news')
    else:
        form = AddPostForm()
    return render(request, 'news/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


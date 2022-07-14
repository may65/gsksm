#from django.core import serializers
from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *



def test(request):
    test = list_fields(Post)
    # return HttpResponse('test')
    return render(request,'forum/test.html',{'test':test})

# def forums(request):
#     """Listing of threads in a forum."""
#     forum = serializers.serialize( "python", Forum.objects.all() )
#     test=forum[1]['pk']
#     table=forum[0]['model']
#     th =['id']
#     th += forum[0]['fields'].keys()
#     td = dict()
#     for d in forum:
#     #     # td.append(d['fields'])
#     #     # td[forum[1]] = d['fields']
#         td.setdefault(d['pk'], d['fields'])
#     return render(request,'forum/forums.html',{'test':test,'forum':forum,'table':table,'th': th,'td':td})

def forum(request):
    pass
    forums = Forum.objects.all().order_by('-date')
    return render(request, 'forum/forum.html', {'forums':forums})

def forum_id(request,forum_id):
    pass
    forum = Forum.objects.get(id=int(forum_id))
    topics = Topic.objects.all().filter(forum=forum_id).order_by('-date')
    return render(request, 'forum/forum_id.html', {'forum_id':forum_id,'forum':forum,'topics':topics})

def topic_id(request,forum_id,topic_id):
    post = Post()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            pass
            post.body = form.cleaned_data['body']
            # post.topic = topic_id
            post.topic = Topic.objects.get(id=int(topic_id))
            post.user = request.user
            # post.
            post.save()
            # return HttpResponseRedirect('/thanks/')
    else:
        form = PostForm()
    pass
    forum = Forum.objects.get(id=int(forum_id))
    topic = Topic.objects.get(id=int(topic_id))
    posts = Post.objects.all().filter(topic=topic_id).order_by('-date')
    return render(request, 'forum/topic_id.html',
                  {'forum_id':forum_id,'topic_id':topic_id,
                   'forum': forum, 'topic': topic,
                   'form':form,'posts':posts})


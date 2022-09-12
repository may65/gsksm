from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.
from django.views import generic

from news.models import Post
from power.models import *

def power(request):
    # line = Line.objects.all()
    # objects_list = line
    # return render(request,'power/power.html')#,{'objects_list':line})
    powers = Power.objects.all().order_by('-time_update')
    # fields = list_fields(Post)
    # field = dir(Post())
    # t = type(field)
    return render(request, 'power/power.html', {'powers':powers,})


def line_list(request):
    td = serializers.serialize( "python", Line.objects.all() )
    th = td[0]['fields'].keys()
    return render(request,'power/list.html',{'title':'Line','th':th,'td':td})

def box_list(request):
    td = serializers.serialize( "python", Box.objects.all() )
    th = td[0]['fields'].keys()
    return render(request,'power/list.html',{'title':'Line','th':th,'td':td})

def count_line(request):
    td = serializers.serialize( "python", CountLine.objects.all() )
    th = td[0]['fields'].keys()
    return render(request,'power/list.html',{'title':'Line','th':th,'td':td})

def count_box(request):
    td = serializers.serialize( "python", CountBox.objects.all() )
    th = td[0]['fields'].keys()
    return render(request,'power/list.html',{'title':'Line','th':th,'td':td})

class LineView(generic.ListView):
    template_name = 'line.html'
    # context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Return lines
        """
        return Line.objects.order_by('line')



from django.shortcuts import render, get_object_or_404

# Create your views here.
from contact.models import Contact


def contact(request):
    ''' Show all news '''
    # print(123)
    # cities = [{'id': 1, 'city': 'Москва'},
    #           {'id': 5, 'city': 'Тверь'},
    #           {'id': 7, 'city': 'Минск'},
    #           {'id': 8, 'city': 'Смоленск'},
    #           {'id': 11, 'city': 'Калуга'}]
    # posts = Post.objects.all().order_by('-time_update')
    # nows = Now.objects.all().order_by('date')
    # fields = list_fields(Post)
    # field = dir(Post())
    # t = type(field)
    # contact = Contact()
    contact = get_object_or_404(Contact, id=1)
    return render(request, 'contact/contact.html', {'contact':contact,})

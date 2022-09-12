from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import TemplateView
from .models import *

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def menuitem():
    menu = {'/gsk/':'ГСК','/news/':'Новости','/forum/':'Форум','/vote/':'Опрос','/l5/':'Электричество','link6':''}
    return menu

# def home(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("User was created successfully.")
#         else:
#             return HttpResponse("There was an error.")
#     else:
#         form = UserForm()
#
#     return render (request, 'vote/home.html', {'form': form})

# print(request)
# class IndexView(generic.ListView):
#     template_name = 'vote/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'vote/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# class ResultsAllView(generic.DetailView):
class VotesAllView(generic.ListView):#, generic.DetailView):
    model = Question
    template_name = 'vote/votes.html'
    # template_name = 'index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class LogAllView(generic.ListView):#, generic.DetailView):
    model = Log
    template_name = 'vote/log.html'
    context_object_name = 'log_vote_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        ord='id'
        if 'order' in self.request.GET:
            ord = self.request.GET['order']
        return Log.objects.all().order_by(ord)

# def test(request):
#     return HttpResponse('<h1>Test Page for test</h1>')
# def testhtml(request):
#     test = Testhtml()
#     test.numb += 1
#     test.save()
#     testall = Testhtml.objects.all()
#     return render(request, 'vote/test.html',{'test':testall,})
# # class TestView(TemplateView):
# #     model = Test
# #     template_name = 'testview.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'vote/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # return HttpResponseRedirect(reverse('voteuser:results', args=(question.id,)))
#         return HttpResponseRedirect(reverse('voteuser:resultsall'))#, args=(question.id,)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'vote/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        if request.user.is_authenticated:
            selected_choice.author = request.user
        else:
            pass
        selected_choice.save()
        log = Log()
        # log = selected_choice
        log.date_vote = selected_choice.date_vote
        log.question = selected_choice.question
        log.author = selected_choice.author
        log.choice_text = selected_choice.choice_text
        log.save()
        # Log().save()
        # return HttpResponseRedirect(reverse('voteuser:results', args=(question.id,)))
        return HttpResponseRedirect(reverse('vote:votes'))#, args=(question.id,)))
        # return render(request,'test.html',{'log':selected_choice})

    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # # votes = models.IntegerField(default=0)
    # date_vote = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.choice_text

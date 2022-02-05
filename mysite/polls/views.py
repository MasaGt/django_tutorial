from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Question, Choise
from django.http import Http404
# Create your views here.


def index(request):
    q_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'q_list': q_list})


def detail(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    # choices = get_list_or_404(Choise, question=q_id)
    return render(request, 'polls/detail.html', {'q': q})


def result(request, q_id):
    return HttpResponse(f'This is result page of {q_id}')


def vote(request, q_id):
    return HttpResponse(f'This is vote page of {q_id}')

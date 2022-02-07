from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.db.models import F
# Create your views here.


def index(request):
    q_list = Question.objects.order_by('-pub_date')
    return render(
                request,
                'polls/index.html',
                {'q_list': q_list}
                )


def detail(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    # choices = get_list_or_404(Choise, question=q_id)
    return render(
                request,
                'polls/detail.html',
                {'q': q}
                )


def result(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    return render(
                request,
                'polls/result.html',
                {'q': q}

    )


def vote(request, q_id):

    q = get_object_or_404(Question, pk=q_id)
    try:
        # get choice object accrding to id in Post
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
                    request,
                    'polls/detail.html',
                    {'q': q,
                     'error_msg': 'Please select a choice'
                     }
                    )
    else:
        # this can cause race condition
        # selected_choice.vote_num += 1
        selected_choice.vote_num = F('vote_num') + 1
        # reload the value of selected_choice
        selected_choice.refresh_from_db() 
        selected_choice.save()
        return HttpResponseRedirect(
                    reverse('polls:result', args=(q_id,))
                    )
        # This is not a good way go to the next page (when POST data is sent)
        return render(
                request,
                'polls/result.html',
                {'q': q}
                )

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # TODO: ↓これは何?
    context_object_name = 'q_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    context_object_name = 'q'
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    context_object_name = 'q'
    template_name = 'polls/result.html'


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
        selected_choice.save()
        # reload the value of selected_choice in database
        selected_choice.refresh_from_db()
        return HttpResponseRedirect(
                    reverse('polls:result', args=(q_id,))
                    )
        # This is not a good way go to the next page (when POST data is sent)
        return render(
                request,
                'polls/result.html',
                {'q': q}
                )

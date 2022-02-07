from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # path(
    #     'url pattern',
    #     a view to show,
    #     name = 'name recognized cross this project'
    #     ),
    path(
        '',
        views.IndexView.as_view(),
        name='index'
        ),
    path(
        'detail/<int:pk>/',
        views.DetailView.as_view(),
        name='detail'
        ),
    path(
        'result/<int:pk>/',
        views.ResultView.as_view(),
        name='result'
        ),
    path(
        'vote/<int:q_id>/',
        views.vote,
        name='vote'
        ),
]

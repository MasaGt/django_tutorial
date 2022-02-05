from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:q_id>/', views.detail, name='detail'),
    path('result/<int:q_id>/', views.result, name='result'),
    path('vote/<int:q_id>/', views.vote, name='vote'),
]

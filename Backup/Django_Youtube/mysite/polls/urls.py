from django.urls import path
from . import views

#Url namespace
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.viewListQuestion, name='question'),
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('<int:question_id>', views.vote, name='vote')
]
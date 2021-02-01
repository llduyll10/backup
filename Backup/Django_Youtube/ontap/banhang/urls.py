from django.urls import path, include
from . import views

app_name='banhang'
urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.QuestionPage, name='list')
]
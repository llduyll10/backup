from django.urls import path, include
from . import views

app_name = 'news'
urlpatterns = [
    #class base view
    path('', views.IndexClass.as_view(), name='index'),
    # path('add/', views.PostClass.as_view(), name='add'),
    path('save/', views.SaveNewClass.as_view(), name='save'),
    path('email/', views.EmailViewClass.as_view(), name='email'),
    path('process/',views.ProcessClass.as_view(), name='process')
]
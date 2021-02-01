from django.urls import path, include
from . import views

app_name = 'Login'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('user-view/', views.ViewUserAuthen.as_view(), name='user-view'),
    path('view-product/', views.view_product, name='view-product'),
    path('add-post', views.AddPost.as_view(), name='add-post')
]

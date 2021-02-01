from django.urls import path
from .views import GetAllCourse

urlpatterns = [
    path('', GetAllCourse.as_view(), name='index'),
]
